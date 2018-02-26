var express = require('express');
var app = express();
var msg='';
var myPythonScriptPath = 'file_sent.py';
var myPythonScriptPath2 = 'tfidf_blob.py';
var myPythonScriptPath3 = 'tfidf_blob1.py';
var myPythonScriptPath_gen = 'fs_sent_general.py';
var message='';
global.textbox='';
global.filename;
global.detected_corpus;
// Use python shell
var PythonShell = require('python-shell');
var fs = require('fs');

app.use(express.static('public'));
app.get('/index2.html', function (req, res) {
   res.sendFile( __dirname + "/" + "index2.html" );
})
app.get('/index.html', function (req, res) {
   res.sendFile( __dirname + "/" + "index.html" );
})
app.get('/loaded.html', function (req, res) {
   res.sendFile( __dirname + "/" + "loaded.html" );
})
app.get('/loading2.html', function (req, res) {
   res.sendFile( __dirname + "/" + "loading2.html" );
})
app.get('/index0.html', function (req, res) {
   res.sendFile( __dirname + "/" + "index0.html" );
})
app.get('/index_general.html', function (req, res) {
   res.sendFile( __dirname + "/" + "index_general.html" );
})
app.get('/process_get', function (req, res) {
   // Prepare output in JSON format
   response = {
      file_name:req.query.file_name,
	  inputtext:req.query.inputtext
   };

   console.log(response);
   
if(req.query.inputtext!='')
{
	global.textbox=req.query.inputtext;
   var path = 'C:/InputFiles/InputText/textbox_040717.txt',
buffer = new Buffer(req.query.inputtext);

fs.open(path, 'w', function(err, fd) {
    if (err) {
        throw 'error opening file: ' + err;
    }

    fs.write(fd, buffer, 0, buffer.length, null, function(err) {
        if (err) throw 'error writing file: ' + err;
        fs.close(fd, function() {
            console.log('file written');
        })
    });
});
global.filename='C:/InputFiles/InputText/';
}
else
{
	global.filename=req.query.file_name;
	global.textbox='';
}
res.sendFile( __dirname + "/" + "loading.html" );

var options = {
  mode: 'text',
  pythonOptions: ['-u'],
  args: [global.filename]
};
PythonShell.run(myPythonScriptPath2 , options, function (err, results) {
  if (err) throw err;
  // results is an array consisting of messages collected during execution
  console.log('results: %j', results);
  global.detected_corpus=results[0];
  console.log(global.detected_corpus);
console.log('file name is : '+global.filename);

});

 //res.end("fin."); 
})
app.get('/loading2', function (req, res) {
   // Prepare output in JSON format
res.sendFile( __dirname + "/" + "loading2.html" );

var options = {
  mode: 'text',
  pythonOptions: ['-u'],
  args: [global.filename]
};

PythonShell.run(myPythonScriptPath , options, function (err, results) {
  if (err) throw err;
  // results is an array consisting of messages collected during execution
  console.log('results: %j', results);

});

 //res.end("fin."); 
})


app.get('/corpus_type',  function (req, res) {
   // Prepare output in JSON format
response = {
      corpus:req.query.corpustype
   };
console.log(response);

var options = {
  mode: 'text',
  pythonOptions: ['-u'],
  args: [global.filename]
};

if(req.query.corpustype=='restaurants' || (req.query.corpustype=='yes'&&global.detected_corpus=='restaurants'))
{
res.sendFile( __dirname + "/" + "loading2.html" );	
PythonShell.run(myPythonScriptPath , options, function (err, results) {
  if (err) throw err;
  // results is an array consisting of messages collected during execution
  console.log('results: %j', results);
//return res.redirect('/index.html');
});
}

else if(req.query.corpustype!='restaurants' && global.detected_corpus!='restaurants')
{
	
res.sendFile( __dirname + "/" + "loading_general.html" );	
PythonShell.run(myPythonScriptPath_gen , options, function (err, results) {
  if (err) throw err;
  // results is an array consisting of messages collected during execution
  console.log('results: %j', results);
//return res.redirect('/index.html');
});
	
	
}

if(req.query.corpustype!='yes')
{
var options1 = {
  mode: 'text',
  pythonOptions: ['-u'],
  args: [global.filename,req.query.corpustype]
};
PythonShell.run(myPythonScriptPath3 , options1, function (err, results) {
  if (err) throw err;
  // results is an array consisting of messages collected during execution
  console.log('results: %j', results);
console.log('file name is : '+global.filename);

});

}
 //res.end("fin."); 
})


var server = app.listen(8081, function () {
   var host = server.address().address
   var port = server.address().port
   console.log("Example app listening at http://%s:%s", host, port)

})