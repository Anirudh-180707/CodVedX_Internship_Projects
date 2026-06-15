# AI Chatbot for Internal Helpdesk

## Overview

The AI Chatbot for Internal Helpdesk is a conversational AI application developed as part of the CodVedX AI/ML Internship Program. The chatbot assists employees by answering frequently asked questions related to company policies, HR services, IT support, attendance, payroll, and other workplace topics.

The system uses intent-based question matching and a structured FAQ dataset to provide relevant responses through a console-based interface.

## Features

* Question-answer chatbot
* Intent-based replies
* FAQ dataset integration
* Admin update capability
* Conversational AI workflow
* CSV-based knowledge base
* Console-based interface
* Exception handling

## Technologies Used

* Python
* Pandas
* Natural Language Processing (NLP) Concepts
* CSV File Handling

## Project Structure

```text
AI_Helpdesk_Chatbot/
│
├── main.py
├── faq_dataset.csv
└── README.md
```

## Dataset

The chatbot uses a custom FAQ dataset containing common employee queries related to:

* Office timings
* Leave management
* IT support
* Attendance
* Payroll
* Company policies
* Training resources
* Employee services

The dataset can be expanded through the chatbot's admin update feature.

## Functionalities

### Ask Question

Allows users to enter a question and receive the most relevant response from the FAQ dataset.

### View FAQs

Displays all available questions and answers stored in the dataset.

### Add FAQ

Allows administrators to add new questions and answers, enabling continuous expansion of the chatbot knowledge base.

### Exit

Closes the chatbot application.

## How to Run

### Install Required Library

```bash
pip install pandas
```

### Run the Application

```bash
python main.py
```

## Sample Usage

Question:

```text
What is the office timing?
```

Response:

```text
Office timing is 9 AM to 6 PM Monday to Friday.
```

Question:

```text
How do I reset my password?
```

Response:

```text
Use the password reset option on the login page.
```

## Learning Outcomes

* NLP Fundamentals
* Intent Detection
* FAQ Dataset Preparation
* Conversational AI Development
* Backend Logic Implementation
* Data Management using CSV Files
* Python Programming
* Git and GitHub Workflow

## Author

Anirudh L

Developed as part of the CodVedX Artificial Intelligence & Machine Learning Internship Program.
