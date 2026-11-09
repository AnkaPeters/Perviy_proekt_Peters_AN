#!/bin/bash

df -h | awk 'NR>1 {if ($5+0 <= 90) print $1, $5; else print $1, $5, "предупреждение"}'
