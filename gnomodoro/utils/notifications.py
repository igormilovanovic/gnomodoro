"""Desktop notifications using Libnotify"""

import gi

gi.require_version("Notify", "0.7")
from gi.repository import Notify


class NotificationManager:
    """Manage desktop notifications"""

    def __init__(self, app_name: str = "Gnomodoro"):
        """Initialize notification manager"""
        self.app_name = app_name
        Notify.init(app_name)
        self.enabled = True

    def send_notification(self, title: str, message: str, urgency: str = "normal") -> None:
        """
        Send a desktop notification.

        Args:
            title: Notification title
            message: Notification message
            urgency: Urgency level (low, normal, critical)
        """
        if not self.enabled:
            return

        notification = Notify.Notification.new(title, message, "dialog-information")
        
        if urgency == "low":
            notification.set_urgency(Notify.Urgency.LOW)
        elif urgency == "critical":
            notification.set_urgency(Notify.Urgency.CRITICAL)
        else:
            notification.set_urgency(Notify.Urgency.NORMAL)

        notification.show()

    def set_enabled(self, enabled: bool) -> None:
        """Enable or disable notifications"""
        self.enabled = enabled

    def cleanup(self) -> None:
        """Clean up notification system"""
        Notify.uninit()
