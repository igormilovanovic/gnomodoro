"""Statistics display dialog"""

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class StatisticsDialog(Gtk.Dialog):
    """Statistics display dialog"""

    def __init__(self, parent, statistics):
        """Initialize statistics dialog"""
        super().__init__(title="Statistics", parent=parent, flags=0)
        self.add_button(Gtk.STOCK_CLOSE, Gtk.ResponseType.CLOSE)
        
        self.statistics = statistics
        
        self.set_default_size(400, 400)
        self.set_border_width(10)
        
        box = self.get_content_area()
        
        # Today's statistics
        today_frame = Gtk.Frame(label="Today")
        today_frame.set_margin_bottom(10)
        box.pack_start(today_frame, False, False, 0)
        
        today_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        today_box.set_border_width(10)
        today_frame.add(today_box)
        
        today_stats = self.statistics.get_today_stats()
        
        count_label = Gtk.Label()
        count_label.set_markup(f"<span font_size='12000'><b>Completed Pomodoros:</b> {today_stats['count']}</span>")
        count_label.set_halign(Gtk.Align.START)
        today_box.pack_start(count_label, False, False, 0)
        
        time_hours = today_stats['total_time'] // 3600
        time_minutes = (today_stats['total_time'] % 3600) // 60
        time_label = Gtk.Label()
        time_label.set_markup(f"<span font_size='12000'><b>Total Time:</b> {time_hours}h {time_minutes}m</span>")
        time_label.set_halign(Gtk.Align.START)
        today_box.pack_start(time_label, False, False, 0)
        
        # Weekly statistics
        week_frame = Gtk.Frame(label="Past 7 Days")
        box.pack_start(week_frame, True, True, 0)
        
        scrolled = Gtk.ScrolledWindow()
        scrolled.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
        week_frame.add(scrolled)
        
        week_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        week_box.set_border_width(10)
        scrolled.add(week_box)
        
        week_stats = self.statistics.get_week_stats()
        
        if not week_stats:
            no_data_label = Gtk.Label(label="No data available")
            no_data_label.set_margin_top(20)
            week_box.pack_start(no_data_label, False, False, 0)
        else:
            for day_stat in week_stats:
                day_row = self._create_day_row(day_stat)
                week_box.pack_start(day_row, False, False, 0)
        
        self.show_all()

    def _create_day_row(self, day_stat):
        """Create a row for daily statistics"""
        row = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        row.set_margin_top(5)
        row.set_margin_bottom(5)
        
        # Date
        date_label = Gtk.Label(label=day_stat["date"])
        date_label.set_size_request(120, -1)
        date_label.set_halign(Gtk.Align.START)
        row.pack_start(date_label, False, False, 0)
        
        # Pomodoros count
        count_label = Gtk.Label(label=f"{day_stat['count']} pomodoros")
        count_label.set_size_request(120, -1)
        count_label.set_halign(Gtk.Align.START)
        row.pack_start(count_label, False, False, 0)
        
        # Time
        total_time = day_stat['total_time']
        hours = total_time // 3600
        minutes = (total_time % 3600) // 60
        time_label = Gtk.Label(label=f"{hours}h {minutes}m")
        time_label.set_halign(Gtk.Align.START)
        row.pack_start(time_label, False, False, 0)
        
        return row
