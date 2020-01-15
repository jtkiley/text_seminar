---
title: 'Self-study track: machine learning'
author: 'Jason T. Kiley'
date: 'January 12, 2020'

geometry: margin=1.1in
fontsize: 12pt
mainfont: 'Source Serif Pro'
monofont: 'Source Code Pro'
urlcolor: 'Blue'

---

# Machine Learning

This machine learning self-study track is designed to start you on the path to a solid practical understanding of machine learning that allows you to train models and get results, followed by an optional deeper dive into the underlying math.

In research, we often use machine learning for some certain types of tasks.
First, we use it to do a good-enough job of labeling data for us that is too time-consuming or poorly-suited for human coding.
For example, instead of classifying tens of thousands of press releases, we can classify up to a few thousand, and use those to train a model to classify the others.
Second, we use unsupervised learning techniques, like k-means clustering or topic models to find groups in observations on the features that we specify.
Then, we have to interpret the meanings of those groupings, which can sometimes reveal something interesting.
This self-study focuses on the former (i.e. supervised learning), not the latter, though there is interesting work done with both.

Because most state-of-the-art results use deep learning---a type of neural network that uses multiple layers to model higher-level features from the input---I have emphasized resources that cover those techniques well.
However, as we discuss in the workshop, start with simpler models and work up to the more complex ones.
Doing so allows you to see what increasingly-complex methods actually gain over simpler methods, and they are part of what you should report in papers (in part to inform future researchers).


# Resources

1. Andrew Ng's [Machine Learning Coursera course](https://www.coursera.org/learn/machine-learning). This course is really well designed, and it is perhaps the most popular machine learning resource (and for good reason). It teaches you a lot of practical concepts with exposure to the underlying math, but without proofs or assuming multivariable calculus. A few tips:
    - The course uses a language called Octave, which is an open source clone of Matlab (which would work, too). Even though you will likely do real work with Python, I suggest using Octave here. In practice, you won't be implementing anything this low level, but it's helpful to understand how things work and why.
    - The course time estimate is about 56 hours in total, and that is fairly accurate overall, though I spend time differently than the individual item estimates. I usually take twice the length of the video (pausing and making notes), and the reading is much faster than estimated.
    - If you are tempted to start running your own data, wait and use `tensorflow`, which is covered in the next item (and does a lot of work for you). Once you're through Week 4 of this course, you could start the next one. However, I suggest working through this course's coverage of a topic before the next one.
1. Coursera [TensorFlow in Practice Specialization courses](https://www.coursera.org/specializations/tensorflow-in-practice) (particularly parts I and III, though the other parts cover some methods with applications on text data). These are very practical courses that walk you through actually using tensorflow to specify and train models. Some notes:
    - I find the estimated times to be much higher than the time I need to complete them. Some sections that are estimated at 3-4 hours only took me about an hour.
    - I suggest using tensorflow 2.0, which these courses support. However, they don't mention some code changes that are necessary. In particular, the new version has friendlier syntax for specifying some parameters, so, for example, you would specify the optimization algorithm using `optimizer='adam'`, not `optimizer=tf.nn.AdamOptimizer()`. The activation functions are also similarly changed in 2.0 (see [documentation](https://www.tensorflow.org/beta/guide/migration_guide)).
1. [Speech and Language Processing](https://web.stanford.edu/~jurafsky/slp3/), 3rd ed. draft, by Jurafsky and Martin. This book is more directly about text and the kinds of features we extract in text, and it also has some coverage of using these methods to get at psychological constructs.
1. Google's [Text classification](https://developers.google.com/machine-learning/guides/text-classification) guide. In particular, look at their advice on choosing a model based on the number of samples and length of text.
1. (optional) If you want to dive deeper into the math-heavy treatments of these topics and want some additional review of the underlying math topics, the [Mathematics for Machine Learning Specialization](https://www.coursera.org/specializations/mathematics-machine-learning) sequence may be helpful.
1. (optional) Read either [*An Introduction to Statistical Learning*](http://faculty.marshall.usc.edu/gareth-james/ISL/) ("ISL") by James, Witten, Hastie, and Tibshirani or [*The Elements of Statistical Learning*](https://web.stanford.edu/~hastie/ElemStatLearn/) ("ESL") by Hastie, Tibshirani, and Friedman. The former is less-math-heavy (and generally more approachable for non-stats/ML PhDs), though it omits coverage of neural networks. Ideally, you would have access to both, but I would read ISL and then look at ESL if you want to go deeper (and for neural networks).
1. (optional) Read [*The Deep Learning Book*](https://www.deeplearningbook.org) by Goodfellow, Bengio, and Courville. This is a math-heavy book that provides through coverage of deep learning specifically. The important part for our purposes is Part II (and, optionally, Part I which should largely be review). Even if the math is a bit abstract at times, the text does a great job of explaining the concepts.
