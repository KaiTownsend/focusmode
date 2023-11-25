# Focus Mode
A desktop Pomodoro Timer-focused application designed to boost productivity by utilizing the Pomodoro technique with many customizable settings such as relaxing background noise, interface, timer settings, and more. The app aims to support students with focus issues or ADHD by helping them stay on track and progress.


### Installation


Before you begin, ensure you have the following installed on your system:
- [Python](https://www.python.org/downloads/) (3.7 or higher)

1. **Download the Application:**
   - Open a terminal (e.g., Command Prompt) and navigate to your preferred installation directory using the following command as an example. Ensure you replace <user> with your current system user name:
     ```
     cd C:\Users\<user>\Downloads 
     ```
   - Download the ZIP file of the application from the GitHub repository or clone it using the following command:
     ```
     git clone https://github.com/KaiTownsend/focusmode.git
     ```
   - Navigate to the directory where you downloaded the files.

2. **Install Required Dependencies:**
   - Install all dependencies listed in the `requirements.txt` file with the following command:
     ```
     pip install -r requirements.txt
     ```

### Running the Application

1. **Start the Application:**
   - Run the following command in your terminal:
     ```
     python main.py
     ```
   - The Focus Mode app should now launch and be ready for use.

### Usage

- **Customize settings:**
  - Use the sliders to adjust the work and break durations to your preference.
  - Use the dropdowns to customize your application's appearance and background noise.
- **Start Focus Session:**
  - Click the 'Start' button to begin a focus session.
- **Take Breaks:**
  - After a work session, take a break as indicated by the timer. The application will automatically transition between work and break periods. 

### Troubleshooting

If you encounter any issues:
- Ensure all steps in the installation guide were followed correctly.
- Check if your Python version is 3.7 or higher.
- If the issue persists, please file an issue on the GitHub repository with a detailed description of the problem.

### Features

- Customizable pomodoro timer settings.
- Persistent settings saved across sessions.
- Background noise options to improve focus.
- Sleek, user-friendly, and customizable interface.
- (Soon) Option to forcefully minimize distractions.

### Credits

- Lilpeanut167 has helped design the project.

### Disclaimers
- This project is heavily in progress, and has multiple missing and broken features.
- Further documentation will be created as this project progresses towards a full release.

### License

- This project is licensed under the Apache 2.0 License.  For more details, see [LICENSE](LICENSE).