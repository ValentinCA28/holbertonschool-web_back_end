const fs = require('fs');

function countStudents(path) {
  try {
    const data = fs.readFileSync(path, 'utf-8');
    const lines = data.split('\n').slice(1);
    console.log(`Number of students: ${lines.length}`);
 
    const students_field = {};
      const first_name = lines[0];
      const field = lines[3];

  } catch (error) {
    throw new Error('Cannot load the database');
  }

}

module.exports = countStudents;