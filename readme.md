 ![image]([[https://github.com/user-attachments/assets/3bbe30c6-b178-45c2-83a7-2316c17a330a](https://media.istockphoto.com/id/1280469581/vector/timer-pomodoro-pomodoro-time-management-kitchen-timer-mechanical-clock-timer-for-working.jpg?s=612x612&w=0&k=20&c=TvE1Dv8YeMvxqMuJb5XJzm5ixEMnWJmkiKACpb4dPDc=)](https://github.com/Azpochita/Pomodoro-Reminder-Bot/blob/main/images/15-Productive-Things-To-Do-During-Pomodoro-Breaks-img.webp))
# Pomodoro Reminder Bot

A bot designed to help you stay on track with your tasks using the Pomodoro technique.

## **TASK MANAGEMENT COMMANDS**

- `!start [task_name]`: Starts a Pomodoro session for the given task.
  - Example: `!start writing_report`
- `!pause`: Pauses the current Pomodoro session.
- `!resume`: Resumes the paused Pomodoro session.
- `!stop`: Stops the current Pomodoro session and resets the timer.
- `!status`: Returns the status of the current session, including time remaining and task name.

## **PROFILE MANAGEMENT COMMANDS**

- `!get_profiles`: Prints out a list of all profiles.
- `!create_profile [profile_name] [member_name1] [member_name2] ...`: Adds all members to the profile for group Pomodoro sessions.
  - Example: `!create_profile team_study alice bob charlie`
- `!delete_profile [profile_name]`: Deletes the profile with the given name.

## **REMINDER COMMANDS**

- `?remind`: Sends a reminder to all members in the current profile that the session is about to start.
- `?nudge [member_name1] [member_name2] ...`: Nudges specific members to join the session.
- `?break`: Notifies everyone in the profile that it’s time for a break.
- `?focus`: Notifies everyone in the profile that it’s time to return to focus mode.

## **RESPONSE COMMANDS**

- `?y`: Confirm participation in the Pomodoro session.
- `?n`: Decline participation in the Pomodoro session.
- `?time [minutes]`: Request an adjustment to the session start time.
  - Example: `?time 5` delays the session by 5 minutes.
- `?clear`: Clears the list of members currently participating in the session.

## **COMMUNICATION COMMANDS**

- `*{OPTIONAL: profile_name} [message]`: Sends a message to all users.
  - Example: `*team_study Let’s start in 5 minutes!`
  - Example: `*Great work everyone!` sends the message to all active users.

## **TIMER MANAGEMENT COMMANDS**

- `!set_pomodoro [minutes]`: Sets the duration of the Pomodoro timer.
  - Example: `!set_pomodoro 25`
- `!set_break [minutes]`: Sets the duration of the break timer.
  - Example: `!set_break 5`
- `!reset`: Resets the timers to their default values.

## **SERVER MANAGEMENT COMMANDS**

- `!start_server {profile_name}`: Starts a collaborative session for the specified profile.
  - **Note:** *Make sure to stop the server afterwards.*
- `!stop_server {profile_name}`: Stops the collaborative session for the specified profile.
- `!get_status {profile_name}`: Retrieves the status of the server for the specified profile.

---

### Default Timers:

- Pomodoro: 25 minutes
- Break: 5 minutes
- Long Break: 15 minutes (after 4 Pomodoro sessions)




