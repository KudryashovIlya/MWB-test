# -*- coding: utf-8 -*-
import unittest

from pages import TopRatingPage
from conf import BASE_URL


class TestCases(unittest.TestCase):

    def setUp(self):
        self.page = TopRatingPage()

    def tearDown(self):
        self.page.close()

    def test_open_page(self):
        """
        Checking that the page is open without any error, title is right, correct url
        """
        page = self.page.open()

        self.assertFalse(self.page.get_browser_errors(), 'Error in browser console')
        self.assertEqual(page.current_url, BASE_URL, 'Wrong url')
        self.assertEqual(page.title, 'IMDb Top 250 - IMDb', 'Wrong title on page')

    def test_add_movie_to_watchlist(self):
        """
        Checking that user can add to watchlist movie
        """
        self.page.sign_in()
        first_movie = self.page.get_first_movie()
        watchList_b = first_movie.find_element_by_xpath('.//td[@class="watchlistColumn"]/div/div')
        watchList_b.click()

        self.assertNotIn('not', watchList_b.get_attribute(name='class'), 'Movie is not added to list')

    def test_rating_and_counter(self):
        """
        Checking that raiting is working and user can put in
        """
        self.page.sign_in()
        first_movie = self.page.get_first_movie()
        rating = first_movie.find_element_by_xpath('.//td[@class="ratingColumn"]/div')
        rating.click()
        counter = self.page.get_rating_counter()

        self.assertNotEqual(rating.text, '', 'No rating')
        self.assertEqual(counter.text, '1', 'Counter not increased')


if __name__ == '__main__':
    unittest.main()

