import uuid

from django.test import TestCase

from data_import.pipeline.examples import Examples
from examples.models import Example
from projects.models import DOCUMENT_CLASSIFICATION
from projects.tests.utils import prepare_project


class TestCategories(TestCase):
    def setUp(self):
        self.project = prepare_project(DOCUMENT_CLASSIFICATION)
        self.example_uuid = uuid.uuid4()
        self.example = Example(uuid=self.example_uuid, text="A", project=self.project.item)
        self.examples = Examples([self.example])

    def test_save(self):
        self.examples.save()
        self.assertEqual(Example.objects.count(), 1)

    def test_getitem(self):
        self.examples.save()
        example = self.examples[self.example_uuid]
        self.assertEqual(example, self.example)
