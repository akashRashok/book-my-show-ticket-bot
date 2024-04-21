# Movie Ticket Availability Checker

This Python script automatically checks for available movie tickets at specified theaters and sends a notification via Telegram when tickets are available. It uses Selenium for web scraping and interacts with the Telegram API for notifications.

## Project Overview

The script monitors ticket availability for the movie "Black Panther: Wakanda Forever" at selected theaters in Kochi. If tickets become available at either "PVR: Lulu, Kochi" or "PVR: Oberon Mall, Kochi", it sends an alert to a specified Telegram chat.

## Key Features

- **Automated Checking**: Continuously checks for ticket availability at specified intervals.
- **Notification**: Sends a message through a Telegram bot when tickets are available.
- **Headless Browsing**: Uses headless Chrome to run the script without UI, suitable for server environments.

## Getting Started

### Prerequisites

- Python 3.x
- Selenium WebDriver
- ChromeDriver
- Requests library

### Environment Setup

1. **Google Chrome**: Ensure Google Chrome is installed on your machine.
2. **ChromeDriver**: Download the appropriate version of ChromeDriver based on your Chrome version from [ChromeDriver Downloads](https://sites.google.com/a/chromium.org/chromedriver/downloads).
3. **Python Libraries**: Install the required Python libraries using pip:
   ```bash
   pip install selenium requests
   
### Configuration

- Set the environment variables GOOGLE_CHROME_BIN and CHROMEDRIVER_PATH to specify the paths to Google Chrome and ChromeDriver respectively.
- Configure your Telegram bot token and chat ID in the script.
- Change the link in the program to the movie you want to book a ticket for.

## Deployment

For continuous operation, consider deploying this script on a server or a cloud instance where you can run long-running Python scripts.
