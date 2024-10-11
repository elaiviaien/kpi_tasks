# Task Overview

## Task 0
- [x] **Prepare GitHub repo** for Tasks.

## Task 1
- [x] **Choose array function** (map/filter/filterMap/some/find/findIndex).
- [x] Prepare its **callback-based async counterpart**.
- [x] Prepare **demo cases** for its usage.
- [x] Add a **new on-demand feature** during review:
  - [x] Add support for **debounce** (if the task took less than X time to complete, add an additional execution delay).
  - [x] Add support for **error handling**.
## Task 2
- [x] Prepare a **promise-based alternative**.
- [x] Write **use cases** for the **promise-based** solution. ( For python, use `asyncio.run`, `asyncio.as_completed` )
- [x] Write **use cases** for the **async-await** solution.
- [x] Add a **new on-demand feature** during review:
  - [x] Add support for **parallelism**. ( For python, use `asyncio.get_running_loop`, `asyncio.run_in_executor`, `asyncio.ThreadPoolExecutor` )

> **Note:** For technologies that do not have native Future-like async functionalities, you may combine Task 1 and 2 into a single task that will showcase the idiomatic way of handling concurrency.

## Task 3
- [x] Integrate **AbortController** or other cancellable approaches. ( For python, use `asyncio.CancelledError` )

## Task 4 (Stream/AsyncIterator/Alternative)
Before running `task4.py` you have to run `gen_million_rows.py` to generate a file with millions of rows.
- [x] Implement ongoing processing of **large data sets** that do not fit in memory.

## Task 5 (Observable/EventEmitter/Alternative)
- [x] Implement **reactive message-based communication** between entities.

---

# Conceptual Notes

### Sync Operations
- if, while, sum, arithmetic

### Async Operations
- API calls, database select, OS access, filesystem (FS) operations

### Synchronous Code Example with Potential Issues
```js
const filesToRead = ["a.txt", "b.txt"];

const a = fs.readFileSync(filesToRead[0]);
const b = fs.readFileSync(filesToRead[1]);

// Issues:
// - Error handling
// - Parallelization
```

### Example of Async Code Using `setTimeout`
```js
setTimeout(() => {}, 1000);
```

### Task Queue: Micro / Macro Tasks

---

# Example of Error Handling in Async Functions (Callback Style)
```js
asyncfns((err, ...data) => {
  if (err !== null) {
    // Process error
    return;
  }
});
```

### Example of Callback Hell
```js
let cb = () => {};
asyncfns1((err, ...data) => {
  if (err !== null) {
    return cb(err);
  }

  asyncfns2(data, (err, ...data) => {
    if (err !== null) {
      // Process error
      return cb(err);
    }

    cb(data);
  });
});
```

### Composition of Async Functions
```js
asyncCompose(asyncfns1, asyncfns2, cb);
```

---

# Task 1: Expected Example of Async Map Function
```js
asyncMap(
  [1, 2, 3],
  (data, cb) => {
    setTimeout(() => {
      cb(null, data * 2);
    }, 1000);
  },
  (err, result) => {
    console.log(err, result); // null [2, 4, 6]
  }
);
```

---

# Additional Concepts

### Sync vs Async Operations

- **Sync Ops:**
  - Control structures like `if`, `while`.
  - Basic arithmetic, such as summing numbers.
  
- **Async Ops:**
  - API calls, file system reads/writes, database queries.
  - Operating system accesses.

### Issues in Sync Operations
- **Error handling:** How to manage unexpected errors.
- **Parallelization:** Running operations concurrently to optimize performance.

### Callback Patterns in Asynchronous Programming
- Nested callback functions can lead to "callback hell" or difficult-to-maintain code.
  
  **Example:**
  ```js
  asyncfns1((err, data1) => {
    if (err) return cb(err);
    asyncfns2(data1, (err, data2) => {
      if (err) return cb(err);
      cb(null, data2);
    });
  });
  ```

### Solution: Function Composition
- Use a function like `asyncCompose` to structure and chain asynchronous tasks cleanly.

  **Example:**c
  ```js
  asyncCompose(asyncfns1, asyncfns2, cb);
  ```