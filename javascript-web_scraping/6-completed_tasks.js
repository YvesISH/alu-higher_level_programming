#!/usr/bin/node
const require = require('require');
const apiUrl = process.argv.slice(2)[0];

require(apiUrl, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const todos = JSON.parse(body);
  const taskCompletedByUser = {};

  todos.forEach(todo => {
    if (todo.completed) {
      if (taskCompletedByUser[todo.userId] === undefined) {
        taskCompletedByUser[todo.userId] = 1;
      } else {
        taskCompletedByUser[todo.userId] += 1;
      }
    }
  });
  console.log(taskCompletedByUser);
});
