# MOROCO-Tweets: The **Mo**ldavian and **Ro**manian Dialectal **Co**rpus of Tweets

## 1. License Agreement

**Copyright (C) 2020 - Mihaela Găman, Radu Tudor Ionescu**

This package contains free data and software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or any later version.

This data set and software is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

 You should have received a copy of the GNU General Public License along with this data set and software (see COPYING.txt package file). If not, see the:
 [GNU License Agreement](http://www.gnu.org/licenses/).


## 2. Citation

Please cite the corresponding work (see citation.bib file to obtain the citation in BibTex format) if you use this data set and software (or a modified version of it) in any scientific work:

**[1] Mihaela Găman, Radu Tudor Ionescu. The Unreasonable Effectiveness of Machine Learning in Moldavian versus Romanian Dialect Identification. International Journal of Intelligent Systems, 2021 [(link to preprint)](https://arxiv.org/abs/2007.15700).**

## 3. Description

#### General Information

The MOROCO-Tweets data set contains Moldavian and Romanian tweets collected from Twitter. 

The data set is divided into two subsets:
- validation (215 samples)
- test (5022 samples)

As training data, users are supposed to use the MOROCO data set. The MOROCO data set and accompanying software is available at:
[https://github.com/butnaruandrei/MOROCO](https://github.com/butnaruandrei/MOROCO)

For each sample, the data set provides corresponding dialectal labels. The samples are preprocessed in order to eliminate named entities. This is required to prevent classifiers from taking the decision based on features that are not related to the dialect or the topics. For example, named entities that refer to city names in Romania or Republic of Moldova can provide clues about the dialect, while named entities that refer to politicians or football players names can provide clues about the topic.

#### Data Organization

The data set is divided in two folders, corresponding to the two subsets for validation and testing. In each subset there are two plain text files:
- ###### dev-target.txt or test.txt

  These files contains one sample per row with the corresponding dialectal label, which are TAB separated. The format of each row is the following:
  ```
  SampleText_1    DialectLabel_1
  SampleText_2    DialectLabel_2
  ...
  SampleText_n    DialectLabel_n
  ```

- ###### dev-target.labels or test.labels

  The dialect_labels.txt file contains one dialect label per row. The format of each row is the following:
  ```
  DialectLabel_1
  DialectLabel_2
  ...
  DialectLabel_n
  ```

  The labels are associated as follows:
  - MD => Moldavian
  - RO => Romanian

The samples and the labels in each file are listed in exactly the same order. This means that, for a given index i (1 <= i <= n), the `SampleText_i` has the dialectal label `DialectLabel_i`.


## 4. Website

The MOROCO-Tweets data set and accompanying software is available at:
[https://github.com/raduionescu/MOROCO-Tweets](https://github.com/raduionescu/MOROCO-Tweets)


## 5. Software Usage

For convenience, we provide Python code to evaluate your model(s).

To evaluate your model(s) on the MOROCO-Tweets data set, use the following command:
```
python eval.py
```
Make sure top place you run files inside the `./Runs` subfolder, before running the evaluation script.

## 6. Feedback

 We are happy to hear your feedback and suggestions at: raducu[dot]ionescu{at}gmail(dot)com
