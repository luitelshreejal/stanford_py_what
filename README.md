# Mentor-Mentee Matching Project using Pywhatkit

This repository contains the implementation of a mentor-mentee matching system developed for a research project at Stanford's Management Science and Engineering (MSE) program. The project utilizes the `pywhatkit` library for efficient and automated matching.

## Overview

The goal of this project is to match mentors with mentees based on predefined criteria, leveraging the `pywhatkit` library for its robust automation capabilities. This system ensures a streamlined and efficient matching process, facilitating better mentorship experiences.

## Features

- **Automated Matching**: Automatically matches mentors with mentees based on specified criteria.
- **Data Handling**: Efficiently processes and manages mentor and mentee data.
- **Notification System**: Uses `pywhatkit` to send notifications and reminders via WhatsApp.
- **Customizable Criteria**: Allows customization of matching criteria to fit different needs and scenarios.

## Installation

To run this project, you'll need to have Python installed on your machine. Follow the steps below to set up the environment:

1. **Clone the repository**:
    ```bash
    git clone https://github.com/luitelshreejal/whatsappautomation.git
    cd whatsappautomation
    ```

2. **Create and activate a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate   # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages (should be obvious just look at the file)**:


## Usage

1. **Prepare Data**: Ensure that your mentor and mentee data is available in the required format. The data should include all necessary details for matching, such as skills, interests, availability, etc.

2. **Configure Matching/ Phone Criteria**: Update the matching criteria in the configuration file or script as per your requirements.

3. **Configure Time "Gap" Criteria**: Update the time gaps between each text sent (Whatsapp requires this to ensure you're not a robot!). 

4. **Run the Matching Script**:
    ```bash
    python MentorMenteeMatchFinal.py
    ```

5. **Notifications**: The system will use `pywhatkit` to send WhatsApp messages to the matched mentors and mentees, notifying them of their pairing.


## Contact

For any questions or inquiries, please contact Shreejal Luitel at his personal cell 911. 

