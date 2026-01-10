#!/bin/bash

# Function to cleanup background processes on exit
cleanup() {
    echo "Stopping all processes..."
    kill $(jobs -p)
}
trap cleanup EXIT

# Start Backend
echo "Starting Backend..."
python src/server.py &
BACKEND_PID=$!
sleep 10

# Start Frontend
echo "Starting Frontend..."
cd dashboard
npm run dev -- --host &
FRONTEND_PID=$!
cd ..

# Wait for Frontend to be ready (checking port 5173)
echo "Waiting for Frontend to be ready on port 5173..."
sleep 5
timeout 60 bash -c 'until echo > /dev/tcp/localhost/5173; do sleep 1; done'

# Run E2E Tests
echo "Running E2E tests..."
pytest tests/test_e2e.py --junitxml=/tmp/test-results.xml
TEST_EXIT_CODE=$?

# Report results
if [ $TEST_EXIT_CODE -eq 0 ]; then
    echo "Tests Passed!"
else
    echo "Tests Failed!"
fi

# Exit with test exit code
exit $TEST_EXIT_CODE
