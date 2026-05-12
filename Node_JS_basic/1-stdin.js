console.log('Welcome to Holberton School, what is your name?');
process.stdin.on('data', (data) => {
  const name = data.toString().trim();
  console.log(`Welcome to Holberton School, ${name}`);
  process.exit();
});
