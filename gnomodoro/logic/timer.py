"""Core Pomodoro Timer Logic"""

import time
from enum import Enum
from typing import Callable, Optional


class TimerState(Enum):
    """Timer state enumeration"""
    IDLE = "idle"
    RUNNING = "running"
    PAUSED = "paused"
    COMPLETED = "completed"


class TimerType(Enum):
    """Timer type enumeration"""
    WORK = "work"
    SHORT_BREAK = "short_break"
    LONG_BREAK = "long_break"


class PomodoroTimer:
    """
    Core Pomodoro Timer class with countdown, pause, and reset functionality.
    """

    def __init__(
        self,
        work_duration: int = 25,
        short_break_duration: int = 5,
        long_break_duration: int = 15,
        pomodoros_until_long_break: int = 4,
    ):
        """
        Initialize the Pomodoro timer.

        Args:
            work_duration: Work session duration in minutes (default: 25)
            short_break_duration: Short break duration in minutes (default: 5)
            long_break_duration: Long break duration in minutes (default: 15)
            pomodoros_until_long_break: Number of pomodoros before long break (default: 4)
        """
        self.work_duration = work_duration * 60  # Convert to seconds
        self.short_break_duration = short_break_duration * 60
        self.long_break_duration = long_break_duration * 60
        self.pomodoros_until_long_break = pomodoros_until_long_break

        self.state = TimerState.IDLE
        self.timer_type = TimerType.WORK
        self.remaining_time = self.work_duration
        self.completed_pomodoros = 0

        # Callbacks
        self.on_tick_callback: Optional[Callable[[int], None]] = None
        self.on_complete_callback: Optional[Callable[[TimerType], None]] = None
        self.on_state_change_callback: Optional[Callable[[TimerState], None]] = None

    def start(self) -> None:
        """Start or resume the timer"""
        if self.state == TimerState.IDLE:
            self.remaining_time = self._get_duration_for_current_type()
        self.state = TimerState.RUNNING
        if self.on_state_change_callback:
            self.on_state_change_callback(self.state)

    def pause(self) -> None:
        """Pause the timer"""
        if self.state == TimerState.RUNNING:
            self.state = TimerState.PAUSED
            if self.on_state_change_callback:
                self.on_state_change_callback(self.state)

    def resume(self) -> None:
        """Resume the timer from paused state"""
        if self.state == TimerState.PAUSED:
            self.state = TimerState.RUNNING
            if self.on_state_change_callback:
                self.on_state_change_callback(self.state)

    def reset(self) -> None:
        """Reset the timer to initial state"""
        self.state = TimerState.IDLE
        self.timer_type = TimerType.WORK
        self.remaining_time = self.work_duration
        if self.on_state_change_callback:
            self.on_state_change_callback(self.state)

    def tick(self) -> bool:
        """
        Decrease timer by one second if running.

        Returns:
            True if timer is still running, False if completed
        """
        if self.state != TimerState.RUNNING:
            return True

        self.remaining_time -= 1

        if self.on_tick_callback:
            self.on_tick_callback(self.remaining_time)

        if self.remaining_time <= 0:
            self._complete_current_timer()
            return False

        return True

    def _complete_current_timer(self) -> None:
        """Handle timer completion and switch to next phase"""
        self.state = TimerState.COMPLETED

        if self.timer_type == TimerType.WORK:
            self.completed_pomodoros += 1
            # Determine next break type
            if self.completed_pomodoros % self.pomodoros_until_long_break == 0:
                self.timer_type = TimerType.LONG_BREAK
            else:
                self.timer_type = TimerType.SHORT_BREAK
        else:
            # After a break, go back to work
            self.timer_type = TimerType.WORK

        if self.on_complete_callback:
            self.on_complete_callback(self.timer_type)

        # Prepare for next timer
        self.remaining_time = self._get_duration_for_current_type()
        self.state = TimerState.IDLE
        if self.on_state_change_callback:
            self.on_state_change_callback(self.state)

    def _get_duration_for_current_type(self) -> int:
        """Get duration in seconds for current timer type"""
        if self.timer_type == TimerType.WORK:
            return self.work_duration
        elif self.timer_type == TimerType.SHORT_BREAK:
            return self.short_break_duration
        else:
            return self.long_break_duration

    def get_remaining_time_formatted(self) -> str:
        """
        Get remaining time as formatted string (MM:SS).

        Returns:
            Formatted time string
        """
        minutes = self.remaining_time // 60
        seconds = self.remaining_time % 60
        return f"{minutes:02d}:{seconds:02d}"

    def set_work_duration(self, minutes: int) -> None:
        """Set work duration"""
        self.work_duration = minutes * 60
        if self.state == TimerState.IDLE and self.timer_type == TimerType.WORK:
            self.remaining_time = self.work_duration

    def set_short_break_duration(self, minutes: int) -> None:
        """Set short break duration"""
        self.short_break_duration = minutes * 60
        if self.state == TimerState.IDLE and self.timer_type == TimerType.SHORT_BREAK:
            self.remaining_time = self.short_break_duration

    def set_long_break_duration(self, minutes: int) -> None:
        """Set long break duration"""
        self.long_break_duration = minutes * 60
        if self.state == TimerState.IDLE and self.timer_type == TimerType.LONG_BREAK:
            self.remaining_time = self.long_break_duration

    def set_on_tick_callback(self, callback: Callable[[int], None]) -> None:
        """Set callback for timer tick"""
        self.on_tick_callback = callback

    def set_on_complete_callback(self, callback: Callable[[TimerType], None]) -> None:
        """Set callback for timer completion"""
        self.on_complete_callback = callback

    def set_on_state_change_callback(self, callback: Callable[[TimerState], None]) -> None:
        """Set callback for state change"""
        self.on_state_change_callback = callback
