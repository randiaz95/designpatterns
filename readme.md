Randy's Software Engineering Design Patterns

## Types of Patterns:
- *Creational*
- *Structural*
- *Behavioral*
- *Concurrency*
- *Architectural*
- *Miscellanious*

# Creational Patterns
- *Factory Method:* Defines an interface for creating an object, but lets subclasses alter the type of objects that will be created.
- *Abstract Factory:* Provides an interface for creating families of related or dependent objects without specifying their concrete classes.
- *Builder:* Separates the construction of a complex object from its representation so that the same construction process can create different representations.
- *Prototype:* Specifies the kinds of objects to create using a prototypical instance, and creates new objects by copying this prototype.
- *Singleton:* Ensures a class has only one instance and provides a global point of access to it.
- *Object Pool:* Manages a pool of reusable objects.
- *Multiton:* A variation of the Singleton pattern that allows for multiple instances.

# Structural Patterns
- *Adapter:* Converts the interface of a class into another interface the client expects. Adapter lets classes work together that couldn’t otherwise because of incompatible interfaces.
- *Bridge:* Separates an object’s abstraction from its implementation so that the two can vary independently.
- *Composite:* Composes objects into tree structures to represent part-whole hierarchies. Composite lets clients treat individual objects and compositions of objects uniformly.
- *Decorator:* Attaches additional responsibilities to an object dynamically. Decorators provide a flexible alternative to subclassing for extending functionality.
- *Facade:* Provides a unified interface to a set of interfaces in a subsystem. Facade defines a higher-level interface that makes the subsystem easier to use.
- *Flyweight:* Uses sharing to support large numbers of fine-grained objects efficiently.
- *Proxy:* Provides a surrogate or placeholder for another object to control access to it.
- *Private Class Data:* Restricts access to class data by using accessor methods.
- *Marker:* Uses empty interfaces to associate metadata with a class.
- *Plain old data object (PODO):* Simplifies the transfer of data by encapsulating it in a single object, often used in serialization, deserialization, and data transport. Other names could be DTO or Data Struct.

# Behavioral Patterns
- *Chain of Responsibility:* Avoids coupling the sender of a request to its receiver by giving more than one object a chance to handle the request.
- *Command:* Encapsulates a request as an object, thereby allowing for parameterization of clients with queues, requests, and operations.
- *Interpreter:* Given a language, defines a representation for its grammar along with an interpreter that uses the representation to interpret sentences in the language.
- *Iterator:* Provides a way to access the elements of an aggregate object sequentially without exposing its underlying representation.
- *Mediator:* Defines an object that encapsulates how a set of objects interact. Mediator promotes loose coupling by keeping objects from referring to each other explicitly.
- *Memento:* Without violating encapsulation, captures and externalizes an object’s internal state so that the object can be restored to this state later.
- *Observer:* Defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.
- *State:* Allows an object to alter its behavior when its internal state changes. The object will appear to change its class.
- *Strategy:* Defines a family of algorithms, encapsulates each one, and makes them interchangeable. Strategy lets the algorithm vary independently from clients that use it.
- *Template Method:* Defines the skeleton of an algorithm in an operation, deferring some steps to subclasses. Template Method lets subclasses redefine certain steps of an algorithm without changing the algorithm’s structure.
- *Visitor:* Represents an operation to be performed on the elements of an object structure. Visitor lets you define a new operation without changing the classes of the elements on which it operates.
- *Publisher/Subscriber (Pubsub):* The Pub-Sub pattern allows senders (publishers) to publish messages to a channel or topic without needing to know who the receivers (subscribers) are. Subscribers express interest in one or more topics and receive messages relevant to those topics without knowing the publishers.

# Concurrency Patterns
- *Active Object:* Decouples method execution from method invocation that reside in their own thread of control.
- *Monitor Object:* An object whose methods are subject to mutual exclusion, ensuring that only one method is executed at a time.
- *Reactor:* A reactor object provides an asynchronous interface to resources that must be handled synchronously.
- *Scheduler:* Provides a way to schedule tasks for future execution.
- *Thread Pool:* Manages a pool of worker threads to efficiently execute asynchronous tasks.
- *Half-Sync/Half-Async:* Divides the processing of a task into two separate layers: synchronous and asynchronous, to allow high-level synchronous operations and low-level asynchronous operations.
- *Read-Write Lock:* Allows concurrent read access to an object but requires exclusive access for writes.

# Architectural Patterns
- *Model-View-Controller (MVC):* Divides an application into three interconnected components: the model (data), the view (user interface), and the controller (business logic).
- *Model-View-ViewModel (MVVM):* Similar to MVC, but separates the view model to provide more manageable and testable code.
- *Layered (n-tier):* Divides the system into layers with specific responsibilities, often including presentation, business logic, and data access layers.
- *Microservices:* Structures an application as a collection of loosely coupled services, which implement business capabilities.
- *Microservices:* Structures an application as a collection of loosely coupled services.
- *Event-Driven Architecture:* Promotes the production, detection, consumption of, and reaction to events.
- *Service-Oriented Architecture (SOA):* An architectural pattern where software components (services) are designed to provide specific functionality over a network. 
- *Layered (N-Tier) Architecture:* Layered architecture, also known as N-Tier architecture, organizes an application into distinct layers, each with specific responsibilities.
- *Client-Server Architecture:* Client-Server architecture is a model where the workload is divided between service providers (servers) and service requesters (clients).
- *Pipe and Filter Architecture:* Pipe and Filter architecture organizes an application into a series of processing stages (filters) connected by data streams (pipes).

# Miscellaneous Patterns
- *Dependency Injection:* A technique where an object receives other objects that it depends on, typically through constructor injection, setter injection, or interface injection.
- *Service Locator:* A pattern used to decouple the interface from the implementation to allow the implementation to change without impacting the users of the interface.
- *Repository:* Encapsulates the logic required to access data sources, centralizing common data access functionality.

# Python Specific Details:

Here are a few design patterns that are generally considered less useful or redundant in Python:

1. Singleton
Why Less Useful: In Python, modules are singleton by default. When a module is imported, it is loaded once and shared across the application, which makes explicit Singleton patterns less necessary.
Alternative: Simply use a module to encapsulate global state or use a class with class-level attributes.
2. Abstract Factory
Why Less Useful: Python’s dynamic typing and the ability to create functions and classes on the fly reduce the need for complex factory patterns.
Alternative: You can often use simple factory functions or leverage Python's dynamic capabilities to create instances as needed without a formal pattern.
3. Prototype
Why Less Useful: Python has a built-in copy module that provides shallow and deep copy functionality, making the Prototype pattern (which involves cloning objects) less relevant.
Alternative: Use copy.copy() or copy.deepcopy() from the copy module.
4. Command
Why Less Useful: The Command pattern is used to encapsulate a request as an object, which can be done easily in Python by passing functions (first-class objects) or using closures.
Alternative: Use higher-order functions or lambdas to achieve similar results without a formal Command pattern.
5. Iterator
Why Less Useful: Python’s iteration protocol, including generators and comprehensions, provides a powerful and flexible way to iterate over collections without needing the explicit Iterator pattern.
Alternative: Use Python's generators or implement the __iter__ and __next__ methods in your classes.
6. Adapter
Why Less Useful: Due to Python's dynamic typing and duck typing, the Adapter pattern is often unnecessary. Objects in Python can be easily adapted or modified at runtime without a formal adapter.
Alternative: Simply modify or extend classes or use duck typing.
7. Strategy
Why Less Useful: The Strategy pattern involves defining a family of algorithms and making them interchangeable. In Python, this can often be achieved more simply by passing functions or using method references.
Alternative: Use function pointers, lambdas, or assign methods dynamically.
8. Observer
Why Less Useful: While the Observer pattern is useful, Python's built-in features like properties, descriptors, and signals in frameworks (e.g., Django signals) reduce the need for an explicit implementation of this pattern.
Alternative: Use event-driven frameworks or Python's built-in mechanisms like property().
9. Memento
Why Less Useful: The Memento pattern, which is used to save and restore an object's state, is often unnecessary due to Python's dynamic nature and the ease with which state can be serialized/deserialized (e.g., using pickle).
Alternative: Use Python’s pickle module or simple dictionaries to save and restore state.