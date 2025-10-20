# Gnomodoro User Guide

## Introduction

Gnomodoro is a Pomodoro timer application designed for the GNOME desktop environment. This guide will help you get started and make the most of the application.

## What is the Pomodoro Technique?

The Pomodoro Technique is a time management method developed by Francesco Cirillo. It uses a timer to break work into intervals, traditionally 25 minutes in length, separated by short breaks. Each interval is known as a "pomodoro."

The technique follows these steps:
1. Choose a task to work on
2. Set the timer for 25 minutes (one pomodoro)
3. Work on the task until the timer rings
4. Take a short break (5 minutes)
5. Every 4 pomodoros, take a longer break (15-30 minutes)

## Getting Started

### Starting a Pomodoro Session

1. Launch Gnomodoro from your application menu
2. The timer will display the default work duration (25:00)
3. Click the "Start" button to begin your first pomodoro
4. Focus on your task until the timer completes
5. When the timer completes, you'll receive a notification
6. Take your break, then start the next pomodoro

### Timer Controls

- **Start**: Begins the timer countdown
- **Pause**: Pauses the current timer (can be resumed)
- **Reset**: Resets the timer to its initial state

## Settings

Access settings by clicking the "Settings" button in the main window.

### Timer Durations

- **Work Duration**: How long each work session lasts (default: 25 minutes)
- **Short Break Duration**: Length of short breaks between work sessions (default: 5 minutes)
- **Long Break Duration**: Length of long breaks after multiple work sessions (default: 15 minutes)
- **Pomodoros Until Long Break**: Number of work sessions before a long break (default: 4)

### Behavior Options

- **Auto-start breaks**: Automatically start break timers when work sessions complete
- **Auto-start work sessions**: Automatically start work timers when breaks complete
- **Enable notifications**: Show desktop notifications when timers complete

### Appearance

Choose between three theme options:
- **System Default**: Uses your system's theme preference
- **Light**: Always use the light theme
- **Dark**: Always use the dark theme

## Task Management

The task management feature helps you track what you're working on during Pomodoro sessions.

### Adding Tasks

1. Click the "Tasks" button in the main window
2. Enter your task name in the text field
3. Click "Add Task" or press Enter

### Managing Tasks

- **Complete a task**: Click the checkmark (✓) button next to the task
- **Delete a task**: Click the X button next to the task

Completed tasks are automatically removed from the active tasks list and recorded in your statistics.

## Statistics

View your productivity statistics by clicking the "Statistics" button.

### Today's Statistics

- Number of completed pomodoros
- Total time spent working

### Weekly Statistics

View the past 7 days of activity:
- Date
- Number of pomodoros completed
- Total time spent

Use this data to:
- Track your productivity trends
- Identify your most productive days
- Set goals for improvement

## Tips for Effective Use

### Best Practices

1. **Plan your tasks**: At the start of each day, list your tasks and estimate how many pomodoros each will take
2. **Eliminate distractions**: During a pomodoro, focus solely on your task
3. **Take breaks seriously**: Use break time to rest, stretch, or do something enjoyable
4. **Adjust durations**: Customize timer lengths to suit your workflow
5. **Track your progress**: Use the statistics feature to see your productivity patterns

### Common Workflows

#### Standard Pomodoro Workflow
1. Start work session (25 minutes)
2. Short break (5 minutes)
3. Repeat 3 more times
4. Long break (15 minutes)
5. Repeat the cycle

#### Customized Workflow
You can adjust the durations to fit your needs:
- Shorter sessions (15 minutes) for highly focused work
- Longer sessions (45 minutes) for deep work
- Longer breaks if you need more recovery time

## Keyboard Navigation

While the application is focused:
- Tab: Navigate between buttons
- Enter/Space: Activate the focused button
- Escape: Close dialogs

## Troubleshooting

### Notifications Not Showing

1. Check that notifications are enabled in Settings
2. Verify that your system allows notifications from Gnomodoro
3. Check your system's notification settings in GNOME Settings

### Timer Not Counting Down

1. Ensure the timer is in "Running" state (Start button should be disabled)
2. Try resetting and starting the timer again
3. Check system resources if the application seems frozen

### Settings Not Saving

Settings are automatically saved when you click "OK" in the Settings dialog. If settings aren't persisting:
1. Check that you have write permissions to `~/.config/gnomodoro/`
2. Ensure your home directory isn't full

### Statistics Not Recording

Statistics are stored in `~/.local/share/gnomodoro/statistics.db`. If data isn't being saved:
1. Check that you have write permissions to this directory
2. Verify the database file isn't corrupted

## Data Locations

- **Settings**: `~/.config/gnomodoro/settings.json`
- **Statistics**: `~/.local/share/gnomodoro/statistics.db`

## Getting Help

If you encounter issues or have questions:
- Check this user guide
- Visit the [GitHub repository](https://github.com/igormilovanovic/gnomodoro)
- Open an issue on GitHub for bug reports or feature requests

## Privacy

Gnomodoro stores all data locally on your computer. No data is transmitted over the network or shared with third parties.
