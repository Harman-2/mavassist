import {defineConfig} from '@playwright/test';
const caps={browser:'chrome',browser_version:'latest',os:'Windows',os_version:'11','browserstack.username':process.env.BROWSERSTACK_USERNAME,'browserstack.accessKey':process.env.BROWSERSTACK_ACCESS_KEY,'browserstack.local':false,project:'MavAssist',build:'course-project',name:'critical flows'};
if(!caps['browserstack.username']||!caps['browserstack.accessKey'])throw new Error('Set BrowserStack credentials and BASE_URL/API_URL for your deployed staging application.');
export default defineConfig({testDir:'./tests',workers:1,timeout:90000,use:{baseURL:process.env.BASE_URL,connectOptions:{wsEndpoint:'wss://cdp.browserstack.com/playwright?caps='+encodeURIComponent(JSON.stringify(caps))}}});
