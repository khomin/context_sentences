const express = require('express');
const data = require('./data/data.json');
const cors = require('cors');

const app = express();

const sql = require('./db/sql');
const { static, json } = require('express');

app.use(cors());

app.use(function(req, res, next){
    console.log(`${req.method} requrest for ${req.url}`);
    next();
});

var last_data = []

var last_num = 0

app.get('/getjson', function(req, res) {
    // var data = {"first_name":"And he set off for the elections without appealing to her for a candid explanation. It was the first time since the beginning of their intimacy that he had parted from her without a full explanation. From one point of view this troubled him, but on the other side he felt that it was better so. “At first there will be, as this time, something undefined kept back, and then she will get used to it. In any case"}
    
    // last_data.push(data)

    // console.log('app.get: ' + req.query.arg)
    
    // // console.log('test: ' + sql.getSentence(req.query.arg))

    // last_data.push(data)

    // res.json(last_data);

    // last_data.push(data)

    // if(req.query.app != null) {
        console.log('app.get: ' + req.query.arg)
    
        sql.getSentence(req.query.arg, (sql_response)=> {
            console.log('test: ' + sql_response)        
            // res.json(sql_response);
            res.json(sql_response);
        })
    // } else {
    //     res.json(last_data);
    // }

    // res.json(last_data);

});

app.set('port', (process.env.PORT || 5000));
app.listen(app.get('port'), function(){
    console.log(`Server is running on port ${app.get('port')}`);
});
