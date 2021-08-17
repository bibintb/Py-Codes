# TensorFlow

In the context of machine learning, tensor refers to the multidimensional array used in the mathematical models that describe neural networks. In other words, a tensor is usually a higher-dimension generalization of a matrix or a vector.

Through a simple notation that uses a rank to show the number of dimensions, tensors allow the representation of complex _n_-dimensional vectors and hyper-shapes as _n_-dimensional arrays. Tensors have two properties: a datatype and a shape.

TensorFlow is an open source deep learning framework that was released in late 2015 under the Apache 2.0 license. Since then, it has become one of the most widely adopted deep learning frameworks in the world (going by the number of GitHub projects based on it).

TensorFlow traces its origins from Google DistBelief, a proprietary production deep learning system developed by the Google Brain project. Google designed TensorFlow from the ground up for distributed processing and to run optimally on Google’s custom application-specific integrated circuit (ASIC) called the Tensor Processing Unit (TPU) in its production data centers. This design makes TensorFlow efficient for deep learning applications.

The framework can run on the CPU, GPU, or TPU on servers, desktops, and mobile devices. Developers can deploy TensorFlow on multiple operating systems and platforms either locally or in the cloud. Many developers consider TensorFlow to have better support for distributed processing and greater flexibility and performance for commercial applications than similar deep learning frameworks such as Torch and Theano, which are also capable of hardware acceleration and widely used in academia.

Deep learning neural networks typically consist of many layers. They transfer data or perform operations between layers using multidimensional arrays. A tensor flows between the layers of a neural network, thus, the name TensorFlow.

The main programming language for TensorFlow is Python. C++, the Java® language, and the Go application programming interface (API) are also available without stability promises, as are many third-party bindings for C#, Haskell, Julia, Rust, Ruby, Scala, R, and even PHP. Google has a mobile-optimized TensorFlow-Lite library to run TensorFlow applications on Android.

This section provides an overview of the TensorFlow system, including the framework’s benefits and applications.



## Benefits of TensorFlow
TensorFlow offers developers:

Eager execution.  
TensorFlow 2 supports eager execution with which operations are evaluated immediately and concrete values are returned, without building graphs. This helps with kick-starting model building and debugging models.

Computational graph model.  
TensorFlow uses data flow graphs called directed graphs to express computational models. This makes it intuitive for developers who can easily visualize what’s going on within the neural network layers by using built-in tools and to perfect their neural network models by adjusting parameters and configurations interactively.

Simple-to-use API.  
Python developers can use either the TensorFlow raw, low-level API, or core API to develop their own models, or use the higher-level API libraries for built-in models. TensorFlow has many built-in and contributed libraries, and it’s possible to overlay a higher-level deep learning framework such as Keras to act as a high-level API. Many of the previous APIs have either been removed or updated to TensorFlow 2.0.

Flexible architecture.  
A major advantage of using TensorFlow is that it has a modular, extensible, and flexible design. Developers can easily move models across CPU, GPU, or TPU processors with few code changes. Although originally designed for large-scale distributed training and inference, developers also can use TensorFlow to experiment with other machine learning models and system optimization of existing models.

Distributed processing.  
Google Brain designed TensorFlow from the ground up for distributed processing on its custom ASIC TPU. In addition, TensorFlow can run on multiple NVIDIA GPU cores. Developers can take advantage of the Intel Xeon and Xeon Phi-based x64 CPU architectures or ARM64 CPU architectures. TensorFlow can run on multi-architecture and multicore systems as well as a distributed process that farms out compute-intensive processing as worker tasks. Developers can create clusters of TensorFlow servers and distribute the computational graph across those clusters for training. TensorFlow can perform distributed training either synchronously or asynchronously, both within the graph and between graphs and can share the common data in memory or across networked compute nodes.

Performance.  
Performance is often a contentious topic, but most developers understand that any deep learning framework depends on the underlying hardware to run optimally to achieve high performance with a low-energy cost. Typically, the native development platform of any framework would achieve the best optimization. TensorFlow performs best on Google TPUs, but it manages to achieve high performance on various platforms-not just servers and desktops but also embedded systems and mobile devices. The framework supports a surprising number of programming languages, as well. Although another framework running natively, such as IBM Watson on the IBM platform, might sometimes outperform TensorFlow, it’s still a favorite with developers because artificial intelligence (AI) projects can span platforms and programming languages targeting multiple end applications, all of which need to produce consistent results.

## TensorFlow applications 
This section looks at the applications that TensorFlow is good at. Obviously, because Google was using its proprietary version of TensorFlow for text and voice search, language translation, and image search applications, the major strengths of TensorFlow are in classification and inference. For example, Google implemented RankBrain, the engine that ranks Google search results, in TensorFlow.

TensorFlow can be used to improve speech recognition and speech synthesis by differentiating multiple voices or filtering speech in high-ambient-noise environments, mimicking voice patterns for more natural-sounding text to speech. Additionally, it handles sentence structure in different languages to produce better translations. It can be used for image and video recognition as well as classification of objects, landmarks, people, sentiments, or activities. This has resulted in major improvements in image and video search.

Because of its flexible, extensible, and modular design, TensorFlow doesn’t limit developers to specific models or applications. Developers have used TensorFlow to implement not only machine learning and deep learning algorithms but also statistical and general computational models. 
