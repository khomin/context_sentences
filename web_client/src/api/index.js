const request = require('request');


// function sendMsg(data, calback) {
//   // request('http://localhost:5000/getjson', { "json": true }, (err, res, body) => {
//   //   if (err) { return console.log(err); }
//   //   console.log(body.url);
//   //   console.log(body.explanation);
//   // });
//   console.log('send msg')
//   request('http://localhost:5000/getjson', { json: true }, (err, res, body) => {
//     if (err) { return console.log(err); }
//     console.log('response: ' + res.body)
//     calback(res.body)
//     // console.log(body.url);
//     // console.log(body.explanation);
//   });
// }

// export { sendMsg };


const https = require('https');

// var connect = https.get('https://jsonplaceholder.typicode.com/users', res => {
//   let data = [];
//   const headerDate = res.headers && res.headers.date ? res.headers.date : 'no response date';
//   console.log('Status Code:', res.statusCode);
//   console.log('Date in Response header:', headerDate);

//   res.on('data', chunk => {
//     data.push(chunk);
//   });

//   res.on('end', () => {
//     console.log('Response ended: ');
//     const users = JSON.parse(Buffer.concat(data).toString());

//     for(user of users) {
//       console.log(`Got user with id: ${user.id}, name: ${user.name}`);
//     }
//   });
// }).on('error', err => {
//   console.log('Error: ', err.message);
// });

function sendMsg(data, calback) {
  console.log('send msg')

  var propertiesObject = { arg: data };

  request({url: 'http://localhost:5000/getjson', qs:propertiesObject}, (err, response, body) => {
    if(err) { console.log(err); return; }
    console.log("Get response: " + response.body);
    calback(JSON.parse(response.body))
  });

  // request('http://localhost:5000/getjson', { json: true }, (err, res, body) => {
  //   if (err) { return console.log(err); }
  //   console.log('response: ' + res.body)
  //   calback(res.body)
  //   // console.log(body.url);
  //   // console.log(body.explanation);
  // });
}

export { sendMsg };

// // api/index.js
// var socket = new WebSocket('ws://localhost:8080/ws');

// let connect = (cb) => {
//   console.log("connecting")

//   socket.onopen = () => {
//     console.log("Successfully Connected");
//   }
  
//   socket.onmessage = (msg) => {
//     console.log("Message from WebSocket: ", msg);
//     cb(msg);
//   }

//   socket.onclose = (event) => {
//     console.log("Socket Closed Connection: ", event)
//   }

//   socket.onerror = (error) => {
//     console.log("Socket Error: ", error)
//   }
// };

// let sendMsg = (msg) => {
//   console.log("sending msg: ", msg);
//   socket.send(msg);
// };

// export { connect, sendMsg };
