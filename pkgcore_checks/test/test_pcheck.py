# Copyright: 2006 Marien Zwart <marienz@gentoo.org>
# License: GPL2


from pkgcore.test import TestCase
from pkgcore.test.scripts import helpers

from pkgcore_checks import pcheck


class UtilitiesTest(TestCase):

    def test_convert_check_filter(self):
        self.assertTrue(pcheck.convert_check_filter('foo')('a.foO.b'))
        self.assertFalse(pcheck.convert_check_filter('foo')('a.foObaR'))
        self.assertFalse(pcheck.convert_check_filter('foo.*')('a.fOoBar'))
        self.assertTrue(pcheck.convert_check_filter('foo.*')('fOoBar'))


class CommandlineTest(TestCase, helpers.MainMixin):

    parser = helpers.mangle_parser(pcheck.OptionParser())
    main = staticmethod(pcheck.main)

    def test_parser(self):
        self.assertError(
            'No target repo specified on commandline or suite and current '
            'directory is not inside a known repo.')
        self.assertError(
            "repo 'spork' is not a known repo (known repos: )",
            '-r', 'spork')
        options = self.parse('spork', '--list-checks')
        self.assertTrue(options.list_checks)
