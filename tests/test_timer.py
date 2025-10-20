"""Unit tests for timer logic"""

import unittest
from gnomodoro.logic.timer import PomodoroTimer, TimerState, TimerType


class TestPomodoroTimer(unittest.TestCase):
    """Test cases for PomodoroTimer class"""

    def setUp(self):
        """Set up test fixtures"""
        self.timer = PomodoroTimer(
            work_duration=25,
            short_break_duration=5,
            long_break_duration=15,
            pomodoros_until_long_break=4
        )

    def test_initial_state(self):
        """Test timer initial state"""
        self.assertEqual(self.timer.state, TimerState.IDLE)
        self.assertEqual(self.timer.timer_type, TimerType.WORK)
        self.assertEqual(self.timer.remaining_time, 25 * 60)
        self.assertEqual(self.timer.completed_pomodoros, 0)

    def test_start_timer(self):
        """Test starting the timer"""
        self.timer.start()
        self.assertEqual(self.timer.state, TimerState.RUNNING)

    def test_pause_timer(self):
        """Test pausing the timer"""
        self.timer.start()
        self.timer.pause()
        self.assertEqual(self.timer.state, TimerState.PAUSED)

    def test_resume_timer(self):
        """Test resuming the timer"""
        self.timer.start()
        self.timer.pause()
        self.timer.resume()
        self.assertEqual(self.timer.state, TimerState.RUNNING)

    def test_reset_timer(self):
        """Test resetting the timer"""
        self.timer.start()
        for _ in range(10):
            self.timer.tick()
        self.timer.reset()
        
        self.assertEqual(self.timer.state, TimerState.IDLE)
        self.assertEqual(self.timer.timer_type, TimerType.WORK)
        self.assertEqual(self.timer.remaining_time, 25 * 60)

    def test_tick_decreases_time(self):
        """Test that tick decreases remaining time"""
        self.timer.start()
        initial_time = self.timer.remaining_time
        self.timer.tick()
        self.assertEqual(self.timer.remaining_time, initial_time - 1)

    def test_timer_completion(self):
        """Test timer completion"""
        self.timer.start()
        
        # Simulate timer completion
        for _ in range(self.timer.remaining_time):
            result = self.timer.tick()
        
        self.assertEqual(self.timer.state, TimerState.IDLE)
        self.assertEqual(self.timer.timer_type, TimerType.SHORT_BREAK)
        self.assertEqual(self.timer.completed_pomodoros, 1)

    def test_long_break_after_four_pomodoros(self):
        """Test that long break occurs after 4 pomodoros"""
        # Complete 3 pomodoros and breaks
        for _ in range(3):
            self.timer.start()
            for _ in range(self.timer.remaining_time):
                self.timer.tick()
            # Skip break
            self.timer.start()
            for _ in range(self.timer.remaining_time):
                self.timer.tick()
        
        # Complete 4th pomodoro
        self.timer.start()
        for _ in range(self.timer.remaining_time):
            self.timer.tick()
        
        self.assertEqual(self.timer.timer_type, TimerType.LONG_BREAK)
        self.assertEqual(self.timer.completed_pomodoros, 4)

    def test_get_remaining_time_formatted(self):
        """Test formatted time string"""
        self.timer.remaining_time = 125  # 2:05
        self.assertEqual(self.timer.get_remaining_time_formatted(), "02:05")
        
        self.timer.remaining_time = 3600  # 60:00
        self.assertEqual(self.timer.get_remaining_time_formatted(), "60:00")

    def test_set_work_duration(self):
        """Test setting work duration"""
        self.timer.set_work_duration(30)
        self.assertEqual(self.timer.work_duration, 30 * 60)
        self.assertEqual(self.timer.remaining_time, 30 * 60)

    def test_set_short_break_duration(self):
        """Test setting short break duration"""
        self.timer.set_short_break_duration(10)
        self.assertEqual(self.timer.short_break_duration, 10 * 60)

    def test_set_long_break_duration(self):
        """Test setting long break duration"""
        self.timer.set_long_break_duration(20)
        self.assertEqual(self.timer.long_break_duration, 20 * 60)

    def test_callbacks(self):
        """Test timer callbacks"""
        tick_called = []
        complete_called = []
        state_change_called = []
        
        def on_tick(remaining):
            tick_called.append(remaining)
        
        def on_complete(next_type):
            complete_called.append(next_type)
        
        def on_state_change(state):
            state_change_called.append(state)
        
        self.timer.set_on_tick_callback(on_tick)
        self.timer.set_on_complete_callback(on_complete)
        self.timer.set_on_state_change_callback(on_state_change)
        
        self.timer.start()
        self.assertTrue(len(state_change_called) > 0)
        
        self.timer.tick()
        self.assertTrue(len(tick_called) > 0)
        
        # Complete timer
        for _ in range(self.timer.remaining_time):
            self.timer.tick()
        
        self.assertTrue(len(complete_called) > 0)
        self.assertEqual(complete_called[0], TimerType.SHORT_BREAK)


if __name__ == "__main__":
    unittest.main()
