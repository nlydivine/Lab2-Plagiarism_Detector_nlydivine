#!/bin/bash

echo "---- Setup started on $(date) ----" >> setup.log

mkdir -p essays reports
echo "Created directories: essays, reports" >> setup.log

if [ ! -f essays/essay1.txt ]; then
    echo "Python is a high-level programming language. It is used in web development, data science, and automation. The language is known for its simplicity and readability." > essays/essay1.txt
    echo "$(date) - Created sample essay1.txt" >> setup.log
fi

if [ ! -f essays/essay2.txt ]; then
    echo "Python programming is popular for web development and data analysis. It is appreciated for its simplicity, readability, and versatility." > essays/essay2.txt
    echo "$(date) - Created sample essay2.txt" >> setup.log
fi

echo "Setup complete!" >> setup.log
echo "---- End of log ----" >> setup.log
echo "Setup complete!"


