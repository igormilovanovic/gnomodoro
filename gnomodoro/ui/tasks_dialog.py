"""Tasks management dialog"""

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class TasksDialog(Gtk.Dialog):
    """Task management dialog"""

    def __init__(self, parent, statistics):
        """Initialize tasks dialog"""
        super().__init__(title="Tasks", parent=parent, flags=0)
        self.add_button(Gtk.STOCK_CLOSE, Gtk.ResponseType.CLOSE)
        
        self.statistics = statistics
        
        self.set_default_size(400, 500)
        self.set_border_width(10)
        
        box = self.get_content_area()
        
        # Add task section
        add_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        add_box.set_margin_bottom(10)
        box.pack_start(add_box, False, False, 0)
        
        self.task_entry = Gtk.Entry()
        self.task_entry.set_placeholder_text("Enter task name...")
        self.task_entry.connect("activate", self.on_add_task)
        add_box.pack_start(self.task_entry, True, True, 0)
        
        add_button = Gtk.Button(label="Add Task")
        add_button.connect("clicked", self.on_add_task)
        add_box.pack_start(add_button, False, False, 0)
        
        # Tasks list
        scrolled = Gtk.ScrolledWindow()
        scrolled.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
        box.pack_start(scrolled, True, True, 0)
        
        self.tasks_box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        scrolled.add(self.tasks_box)
        
        self._refresh_tasks()
        
        self.show_all()

    def on_add_task(self, widget):
        """Add a new task"""
        task_name = self.task_entry.get_text().strip()
        if task_name:
            self.statistics.add_task(task_name)
            self.task_entry.set_text("")
            self._refresh_tasks()

    def _refresh_tasks(self):
        """Refresh the tasks list"""
        # Clear existing tasks
        for child in self.tasks_box.get_children():
            self.tasks_box.remove(child)
        
        # Get active tasks
        tasks = self.statistics.get_active_tasks()
        
        if not tasks:
            no_tasks_label = Gtk.Label(label="No active tasks")
            no_tasks_label.set_margin_top(20)
            self.tasks_box.pack_start(no_tasks_label, False, False, 0)
        else:
            for task in tasks:
                task_row = self._create_task_row(task)
                self.tasks_box.pack_start(task_row, False, False, 0)
        
        self.tasks_box.show_all()

    def _create_task_row(self, task):
        """Create a row for a task"""
        row = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
        row.set_margin_top(5)
        row.set_margin_bottom(5)
        
        # Task name
        task_label = Gtk.Label(label=task["name"])
        task_label.set_halign(Gtk.Align.START)
        task_label.set_line_wrap(True)
        row.pack_start(task_label, True, True, 0)
        
        # Complete button
        complete_button = Gtk.Button(label="✓")
        complete_button.set_size_request(40, 30)
        complete_button.connect("clicked", self.on_complete_task, task["id"])
        row.pack_start(complete_button, False, False, 0)
        
        # Delete button
        delete_button = Gtk.Button(label="✗")
        delete_button.set_size_request(40, 30)
        delete_button.connect("clicked", self.on_delete_task, task["id"])
        row.pack_start(delete_button, False, False, 0)
        
        return row

    def on_complete_task(self, button, task_id):
        """Mark task as completed"""
        self.statistics.complete_task(task_id)
        self._refresh_tasks()

    def on_delete_task(self, button, task_id):
        """Delete a task"""
        self.statistics.delete_task(task_id)
        self._refresh_tasks()
