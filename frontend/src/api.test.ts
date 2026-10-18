// @vitest-environment jsdom
import {afterEach,expect,test,vi} from 'vitest';
import {api,json} from './api';
afterEach(()=>{sessionStorage.clear();vi.restoreAllMocks();});
test('authenticated requests attach the session token and JSON body',async()=>{
 sessionStorage.setItem('mavassist-token','token');const fetchMock=vi.spyOn(globalThis,'fetch').mockResolvedValue(new Response(JSON.stringify({ok:true}),{status:200}));
 expect(await api('/api/test',json('POST',{a:1}))).toEqual({ok:true});expect(fetchMock.mock.calls[0][1]?.headers).toMatchObject({'Authorization':'Bearer token','Content-Type':'application/json'});
});
test('expired sessions clear credentials and notify the app',async()=>{
 sessionStorage.setItem('mavassist-token','expired');const listener=vi.fn();window.addEventListener('session-expired',listener);
 vi.spyOn(globalThis,'fetch').mockResolvedValue(new Response(JSON.stringify({detail:'Expired'}),{status:401}));await expect(api('/api/bookmarks')).rejects.toThrow('Expired');expect(sessionStorage.getItem('mavassist-token')).toBeNull();expect(listener).toHaveBeenCalledOnce();window.removeEventListener('session-expired',listener);
});
