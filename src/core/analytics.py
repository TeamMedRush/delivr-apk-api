from asyncio import create_task, to_thread

from os import getenv

from mixpanel import Mixpanel, Consumer

MIXPANEL_TOKEN = getenv("MIXPANEL_TOKEN")
mixpanel_client = Mixpanel(
  MIXPANEL_TOKEN,
  consumer=Consumer(
    api_host="api-eu.mixpanel.com",
  )
)

class Analytics:
  def _track(
    user_id: str,
    event_name: str,
    properties: dict = None,
  ):
    """
    Track an event for a specific user.
    """

    if properties is None:
      properties = {}

    mixpanel_client.track(
      user_id,
      event_name,
      properties,
    )

  def _profile(
    user_id: str,
    properties: dict,
  ):
    """
    Update the user profile with the provided properties.
    """
    mixpanel_client.people_set(
      user_id,
      properties,
    )

  @staticmethod
  def track_event(
    user_id: str,
    event_name: str,
    properties: dict = None,
  ):
    """
    Track an event for a specific user.
    """
    create_task(
      to_thread(
        Analytics._track,
        *(user_id, event_name, properties)
      )
    )

  @staticmethod
  def track_user_profile(
    user_id: str,
    properties: dict,
  ):
    """
    Update the user profile with the provided properties.
    """
    create_task(
      to_thread(
        Analytics._profile,
        *(user_id, properties)
      )
    )

