import asyncio
import time

# A simple async function that simulates a "long-running" operation.
# For example, it could be a call to an external API or service.
async def do_something(name):
    print(f"Starting {name}...")
    # This line simulates work that takes 1 second to complete.
    await asyncio.sleep(1)
    print(f"Finished {name}!")

async def main():
    print("Creating tasks...")
    # Create two tasks, which can run concurrently
    task1 = asyncio.create_task(do_something("Task 1"))
    task2 = asyncio.create_task(do_something("Task 2"))

    print("Waiting for tasks to complete...")
    # Wait for both tasks to finish
    await task1
    await task2
    print("All tasks done!")

if __name__ == "__main__":
    start = time.time()
    # Run the main() async function in an event loop
    asyncio.run(main())
    end = time.time()
    print(f"Total time elapsed: {end - start:.2f} seconds")
