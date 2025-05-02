import unittest
import entertainment1

class EntertainmentSystemTests(unittest.TestCase):
  # Checkpoint 1
  @unittest.skipIf(entertainment1.regional_jet(), 'Not available on regional jets')
  def test_movie_license(self):
    daily_movie = entertainment1.get_daily_movie()
    licensed_movies = entertainment1.get_licensed_movies()
    self.assertIn(daily_movie, licensed_movies)

  # Checkpoint 2
  @unittest.skipUnless(entertainment1.regional_jet() is False, 'Not available on regional jets')
  def test_wifi_status(self):
    wifi_enabled = entertainment1.get_wifi_status()
    self.assertTrue(wifi_enabled)

  # Checkpoint 3
  def test_device_temperature(self):
    if entertainment1.regional_jet():
      self.skipTest('Not available on regional jets')
    device_temp = entertainment1.get_device_temp()
    self.assertLess(device_temp, 35)

  # Checkpoint 3
  def test_maximum_display_brightness(self):
    if entertainment1.regional_jet():
      self.skipTest('Not available on regional jets')
    brightness = entertainment1.get_maximum_display_brightness()
    self.assertAlmostEqual(brightness, 400)


unittest.main()
