@title[Hadoop]
## Hadoop

+++
@title[Hadoop]
<span style="color:gray; font-size:1em">Hadoop </span>
- "__The ApacheTM HadoopTM__" project develops open-source software for fault-tolerant, scalable and distributed computing.

+++
@title[Features]
<span style="color:gray; font-size:1em">Features </span>
- Works with BigData on regular servers
- Implements the logic of MapReduce
- Strong open-source community

+++
@title[Hadoop Principles]
<span style="color:gray; font-size:1em">Hadoop Principles </span>

- Scale-Out
- Compute should move to data
- Fault Tolerance
- Simple core, modular and extensible

---
@title[MapReduce]
## MapReduce

+++
@title[MapReduce]
<span style="color:gray; font-size:1em">MapReduce </span>

* a programming model and
* an associated implementation
* for processing and generating big data sets
* with a parallel, distributed algorithm
* on a cluster.

+++
@title[MapReduce Paradigm]

<span style="color:gray; font-size:0.7em">MapReduce Paradigm </span>

![Image-Absolute](pics/map-reduce-1.png)

+++
@title[MapReduce Stages]
<span style="color:gray; font-size:0.7em">MapReduce Stages </span>

* __Map__
    * Converts source elements to pairs (key, value)
* __Shuffle__
    * Sorts data by the keys and distributes it to the reducers
* __Reduce__
    * Aggregates data by key

---
@title[Classic MapReduce Example: WordCount]

<span style="color:gray; font-size:0.7em"> Classic MapReduce Example: WordCount </span>

![Image-Absolute](pics/wordcount-schematic.png)

+++
@title[Python WordCount Realisation #1]
<p><span class="menu-title slide-title">WordCount mapper.py</span></p>

```python
import sys

for line in sys.stdin:
    for word in line.strip().split():
        print(word + "\t1")
```

@[3](Read every line from input.)
@[4](Clean text.)
@[5](Create Key-Value Pair.)

+++
@title[Python WordCount Realisation #2]
<p><span class="menu-title slide-title">WordCount reducer.py</span></p>

```python
import sys

last_key = None
values_sum = 0

for line in sys.stdin:
    key, value = line.strip().split("\t")
    if key != last_key and last_key is not None:
        print(last_key + "\t" + str(values_sum))
        values_sum = 0
    last_key = key
    values_sum += int(value)

if key != last_key and last_key is not None:
    print(last_key + "\t" + str(values_sum)) 
```

@[6](Read every line from input.)
@[7](Get key and value from line.)
@[8-12](While key doesn't change accumulate counts for one key.)

@title[Python WordCount Realisation #3]
<p><span class="menu-title slide-title">WordCount: Bash Debugging</span></p>

```bash
cat document.txt | 
python mapper.py | 
sort -k 1,1 | 
python reducer.py > output.txt
```

@[1](Read document.)
@[2](Implement Map part.)
@[3](Sort all Key-Value Pairs by keys.)
@[4](Implement Reduce part and save to output file.)

@title[Python WordCount Realisation #4]
<p><span class="menu-title slide-title">WordCount: Hadoop Streaming</span></p>

```bash
hadoop jar hadoop-streaming.jar
-input myinput
-output myoutput
-mapper /path/to/mapper.py
-reducer /path/to/reducer.py
```

@[1](Run Hadoop streaming jar.)
@[2](Set in parameters input folder.)
@[3](Set in parameters output folder.)
@[4](Set path to the mapper.)
@[5](Set path to the reducer.)

+++
@title[Multiple rounds of the MapReduce]

<span style="color:gray; font-size:0.7em"> Multiple rounds of the MapReduce </span>

![Image-Absolute](pics/map-reduce-2.png)

