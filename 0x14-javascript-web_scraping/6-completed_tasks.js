#!/usr/bin/node

const request = require('request');

request(process.argv[2], (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const result = {};
    const todos = JSON.parse(body);
    for (const todo of todos) {
      if (todo.completed === true) {
        if (!result[String(todo.userId)]) {
          result[String(todo.userId)] = 1;
        } else {
          result[String(todo.userId)]++;
        }
      }
    }
    console.log(result);
  }
});
