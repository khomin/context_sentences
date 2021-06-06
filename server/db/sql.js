const sqlite3 = require('sqlite3')

const db = new sqlite3.Database('../db_service/sqlite.db');

function getSentence(arg, callback) {
    if(arg != undefined) {
        var query = "SELECT * FROM Texts WHERE Body LIKE '%" + arg + "%' LIMIT 15;"
        db.all(query, (error, rows) => {
            var res = []
            rows.forEach((row) => {
                console.log(row.body);

                var reply = row.body.toLowerCase()

                var split = reply.split(arg.toLowerCase())
                if(split.length >= 2) {
                    var obj = new Object()
                    obj.number = res.length
                    obj.left_part_of_sentence = split[0]
                    obj.right_part_of_sentence = split[1]
                    obj.key_sentence = arg
                    res.push(obj)
                }
            })
            callback(res)
        });
    }
}

module.exports = { getSentence };