#!/usr/bin/node
const requ = require('require');
const apiUrl = process.argv.slice(2)[0];

requ(apiUrl, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const todos = JSON.parse(body);
  const taskCompletedByUser = {};

  todos.forEach(todo => {
    if (todo.completed) {
      if (taskCompletedByUser[todo.userId]) {
        taskCompletedByUser[todo.userId] = 1;
      }
    }
  });
  object.entries(taskCompletedByUser).forEach(([userId, count]) => {
    console.log(`user Id: ${userId}, Tasks completed: ${count}`);
  });
});
