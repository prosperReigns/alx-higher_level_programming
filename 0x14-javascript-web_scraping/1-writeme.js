#!/usr/bin/node

const fs = require('fs');
// Import the built-in Node.js 'fs' module.

fs.readFile(process.argv[2], 'utf8', function (error, content) {
  // Use fs.readFile() to read the contents of a file specified as a command-line argument
  // 'utf8' specifies the encoding of the file being read

  if (error) {
    // If an error occurs during the file read operation, the 'error' parameter will contain an error object.
    console.error('Error reading the file:', error);

  } else {
    // If the file is read successfully, the 'content' parameter will contain the contents of the file as a string.
    console.log(content);
  }
});

0x14-javascript-web_scraping/1-writeme.js

#!/usr/bin/node

const fs = require('fs');
// Import the built-in Node.js 'fs' module.

fs.writeFile(process.argv[2], process.argv[3], 'utf8', error => {
  // Use fs.writeFile() to write data to a file specified as the third command-line argument (process.argv[2]).
  // The data to be written is taken from the fourth command-line argument (process.argv[3]).

  if (error) {
    // If an error occurs during the write operation, the 'error' parameter will contain an error object.
    console.error(error);
  }
});
