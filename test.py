#!/usr/bin/env python
# -*- coding: utf-8 -*-

import lib.calendario as cal

for i in range(15):
    sg = cal.SEMANAS_GESTACAO[i]
    print i + 1, sg

print cal.BETA_HCG

print cal.qual_semana_gestacao( cal.hoje() )