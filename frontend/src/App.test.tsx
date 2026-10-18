// @vitest-environment jsdom
import {afterEach,expect,test,vi} from 'vitest';
import {cleanup,fireEvent,render,screen,waitFor} from '@testing-library/react';
import App from './App';
afterEach(()=>{cleanup();sessionStorage.clear();vi.restoreAllMocks();});
test('registration form uses labels and submits only student fields',async()=>{
 const fetchMock=vi.spyOn(globalThis,'fetch').mockResolvedValue(new Response(JSON.stringify({detail:'Test registration rejected'}),{status:422}));
 render(<App/>);fireEvent.click(screen.getByRole('button',{name:'Create an account'}));
 fireEvent.change(screen.getByLabelText('Full name'),{target:{value:'Demo Student'}});fireEvent.change(screen.getByLabelText('Email address'),{target:{value:'demo@example.com'}});fireEvent.change(screen.getByLabelText('Password'),{target:{value:'Student-pass123!'}});
 fireEvent.submit(screen.getByRole('button',{name:'Create student account'}).closest('form')!);
 await waitFor(()=>expect(screen.getByRole('alert').textContent).toContain('Test registration rejected'));
 expect(JSON.parse(String(fetchMock.mock.calls[0][1]?.body))).toEqual({name:'Demo Student',email:'demo@example.com',password:'Student-pass123!'});
});
