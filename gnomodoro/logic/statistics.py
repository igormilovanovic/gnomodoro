"""Statistics tracking for Gnomodoro"""

import json
import sqlite3
from datetime import datetime, date
from pathlib import Path
from typing import List, Dict, Optional


class Statistics:
    """Track and manage Pomodoro statistics"""

    def __init__(self):
        """Initialize statistics database"""
        self.data_dir = Path.home() / ".local" / "share" / "gnomodoro"
        self.data_dir.mkdir(parents=True, exist_ok=True)
        self.db_path = self.data_dir / "statistics.db"
        self._init_database()

    def _init_database(self) -> None:
        """Initialize the database schema"""
        conn = sqlite3.connect(str(self.db_path))
        cursor = conn.cursor()
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS pomodoros (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT NOT NULL,
                timestamp TEXT NOT NULL,
                duration INTEGER NOT NULL,
                task TEXT
            )
        """)
        
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                created_at TEXT NOT NULL,
                completed BOOLEAN DEFAULT 0,
                completed_at TEXT
            )
        """)
        
        conn.commit()
        conn.close()

    def add_completed_pomodoro(self, duration: int, task: Optional[str] = None) -> None:
        """Record a completed Pomodoro"""
        conn = sqlite3.connect(str(self.db_path))
        cursor = conn.cursor()
        
        today = date.today().isoformat()
        now = datetime.now().isoformat()
        
        cursor.execute(
            "INSERT INTO pomodoros (date, timestamp, duration, task) VALUES (?, ?, ?, ?)",
            (today, now, duration, task)
        )
        
        conn.commit()
        conn.close()

    def get_today_stats(self) -> Dict[str, int]:
        """Get statistics for today"""
        conn = sqlite3.connect(str(self.db_path))
        cursor = conn.cursor()
        
        today = date.today().isoformat()
        
        cursor.execute(
            "SELECT COUNT(*), SUM(duration) FROM pomodoros WHERE date = ?",
            (today,)
        )
        result = cursor.fetchone()
        
        conn.close()
        
        count = result[0] if result[0] else 0
        total_time = result[1] if result[1] else 0
        
        return {
            "count": count,
            "total_time": total_time,
        }

    def get_week_stats(self) -> List[Dict[str, any]]:
        """Get statistics for the past 7 days"""
        conn = sqlite3.connect(str(self.db_path))
        cursor = conn.cursor()
        
        cursor.execute("""
            SELECT date, COUNT(*) as count, SUM(duration) as total_time
            FROM pomodoros
            WHERE date >= date('now', '-7 days')
            GROUP BY date
            ORDER BY date DESC
        """)
        
        results = cursor.fetchall()
        conn.close()
        
        return [
            {
                "date": row[0],
                "count": row[1],
                "total_time": row[2]
            }
            for row in results
        ]

    def add_task(self, name: str) -> int:
        """Add a new task"""
        conn = sqlite3.connect(str(self.db_path))
        cursor = conn.cursor()
        
        now = datetime.now().isoformat()
        cursor.execute(
            "INSERT INTO tasks (name, created_at) VALUES (?, ?)",
            (name, now)
        )
        
        task_id = cursor.lastrowid
        conn.commit()
        conn.close()
        
        return task_id

    def complete_task(self, task_id: int) -> None:
        """Mark a task as completed"""
        conn = sqlite3.connect(str(self.db_path))
        cursor = conn.cursor()
        
        now = datetime.now().isoformat()
        cursor.execute(
            "UPDATE tasks SET completed = 1, completed_at = ? WHERE id = ?",
            (now, task_id)
        )
        
        conn.commit()
        conn.close()

    def get_active_tasks(self) -> List[Dict[str, any]]:
        """Get all active (non-completed) tasks"""
        conn = sqlite3.connect(str(self.db_path))
        cursor = conn.cursor()
        
        cursor.execute(
            "SELECT id, name, created_at FROM tasks WHERE completed = 0 ORDER BY created_at DESC"
        )
        
        results = cursor.fetchall()
        conn.close()
        
        return [
            {
                "id": row[0],
                "name": row[1],
                "created_at": row[2]
            }
            for row in results
        ]

    def delete_task(self, task_id: int) -> None:
        """Delete a task"""
        conn = sqlite3.connect(str(self.db_path))
        cursor = conn.cursor()
        
        cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        
        conn.commit()
        conn.close()
