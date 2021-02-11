# nbexecutor

아주 오~래 걸리는 노트북 파일들을 일괄적으로 실행하기 위한 모듈  
python 스크립트로 노트북 파일을 실행시키고, 실행된 노트북 결과를 `executed/` 폴더에 저장한다.  
만약 실행 중 오류가 나면 오류를 raise 하며 스크립트 실행을 중지한다.
오류 결과는 실행결과와 마찬가지로 `executed/` 폴더에 저장된다.


# Installation

```
git clone https://github.com/pparkddo/nbexecutor.git
```

# Example

```python
from datetime import datetime
from os.path import basename, join
from glob import glob

from nbexecutor import execute_notebook


excludes = set([basename(each) for each in glob(join("executed", "*.ipynb"))])
executables = [each for each in glob("*.ipynb") if each not in excludes]
for each in executables:
    print(f"{datetime.now():%Y-%m-%d %H:%M:%S} Running {each}...")
    execute_notebook(each)
```

Output
```
2021-01-18 07:16:02 Running README.ipynb...
2021-01-18 07:20:15 Running 0-1. Unzip.ipynb...
2021-01-18 07:39:12 Running 0-1-1. Outliers.ipynb...
2021-01-18 07:45:43 Running 0-2. Make Concatenated Data File.ipynb...
...
2021-01-18 08:40:54 Running 5-0-3. Classify Charge Period.ipynb...
2021-01-18 09:16:21 Running 5-0-4. Merge Master Table.ipynb...
2021-01-18 09:25:04 Running 5-0-5. Merge Meter Day.ipynb...
2021-01-18 09:37:33 Running 5-1. Get MDMS Result with Average Pattern.ipynb...
```
