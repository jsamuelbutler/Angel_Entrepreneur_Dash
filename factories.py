from __future__ import unicode_literals

import factory


class AcceleratorFactory(factory.django.DjangoModelFactory):
    name = factory.Sequence(lambda n: "Accelerator {}".format(n))
    website = 'http://example.com'

    class Meta:
        model = 'accelerators.Accelerator'


class CohortFactory(factory.django.DjangoModelFactory):
    name = factory.Sequence(lambda n: "Cohort {}".format(n))
    accelerator = factory.SubFactory(AcceleratorFactory)

    class Meta:
        model = 'accelerators.Cohort'
