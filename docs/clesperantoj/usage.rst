How to use
==========

Get a device
-------------

All GPU operations must be executed on a specific device. Before running operations, you need to select which device (GPU or CPU) to use.
clesperantoJ rely on the class `DeviceJ` and the method `getDevice()` to get a specific device.

.. code:: java

    import net.clesperanto.core.DeviceJ;

    public class MyExampleCode {
        public static void main(String[] args) {
            // ... some code ...
            DeviceJ device = DeviceJ.getDefaultDevice();   // Get the default device of your system
            // ... some code ...
        }
    }

You can also specify the device by providing a substring to identify it and a type ("gpu", "cpu", etc.).

.. code:: java

    DeviceJ device = DeviceJ.getDevice("NVIDIA", "gpu");   // Get the first "NVIDIA" GPU device


Data transfer
-------------

The main data structure in clesperantoJ is `ArrayJ`, which represents a buffer stored on a device.
It allows you to allocate, read, write, and manipulate data on the selected device.
The interface with the host (CPU) memory is done through standard Java arrays.

Create
~~~~~~

We can allocate a buffer on the device using the static method `create()` of the `ArrayJ` class.

.. code:: java

    import net.clesperanto.core.DeviceJ;
    import net.clesperanto.core.ArrayJ;
    import net.clesperanto.core.MemoryType;
    import net.clesperanto.core.DataType;

    public class MyExampleCode {
        public static void main(String[] args) {
            // ... some code ...
            ArrayJ array = ArrayJ.create([3, 3, 2], device, DataType.FLOAT, MemoryType.BUFFER);   // Allocate array of shape 3x3x2 on device
            // ... some code ...        
        }
    }

`MemoryType` and `DataType` are enums that allow you to specify the type of memory (BUFFER, IMAGE, etc.) and the data type (FLOAT, INT, etc.) of the ArrayJ.
The new ArrayJ object is, by default, empty (uninitialized data) and can be used to store future outputs of GPU operations or will need to be filled with data from the host.

Push
~~~~

The `push` is the transfert from the host to the device. This is done using the method `writeFromArray()` of the `ArrayJ` class to write host data to a buffer on the device.

.. code:: java

    import net.clesperanto.core.DeviceJ;
    import net.clesperanto.core.ArrayJ;
    import net.clesperanto.core.MemoryType;
    import net.clesperanto.core.DataType;

    public class MyExampleCode {
        public static void main(String[] args) {
            // ... some code ...
            float data[] = new float[3 * 3 * 2];                                                    // Allocate host memory
            data.fill(1.0f);     
            ArrayJ array = ArrayJ.create([3, 3, 2], device, DataType.FLOAT, MemoryType.BUFFER);     // Allocate array on device
            array.writeFromArray(data);                                                             // Write data from host to device
            // ... some code ...        
        }
    }

The receiving ArrayJ must have been allocated ahead of time with the correct shape and data type.

Pull
~~~~

The `pull` is the transfert from the device to the host. This is done using the method `readToArray()` of the `ArrayJ` class to read device data to a buffer on the host.

.. code:: java

    import net.clesperanto.core.DeviceJ;
    import net.clesperanto.core.ArrayJ;
    import net.clesperanto.core.MemoryType;
    import net.clesperanto.core.DataType;

    public class MyExampleCode {
        public static void main(String[] args) {
            // ... some code ...
            ArrayJ array = ArrayJ.create([3, 3, 2], device, DataType.FLOAT, MemoryType.BUFFER);     // Allocate array on device
            // ... some code to fill the array on device ...
            float data[] = new float[3 * 3 * 2];                                                    // Allocate host memory
            array.readToArray(data);                                                                // Read data from device to host
            // ... some code ...        
        }
    }

The receiving host array must have been allocated ahead of time with the correct size and data type.

Converters
~~~~~~~~~~ 

clesperantoJ provides converters to facilitate the creation of `ArrayJ` objects from common scientific Java libraries such as ImageJ and ImgLib2.
These converters simplify the process of transferring data between host and device by handling the necessary conversions automatically, including the device memory allocation.


** From ImageJ and ImgLib2 to ArrayJ**
.. code:: java

    import net.clesperanto.core.DeviceJ;
    import net.clesperanto.core.ArrayJ;
    import net.clesperanto.core.MemoryType;
    import net.clesperanto.imagej.ImageJConverters;
    import net.clesperanto.imglib2.ImgLib2Converters;

    import net.imglib2.RandomAccessibleInterval;
    import ij.ImagePlus;

    public class MyExampleCode {
        public static void main(String[] args) {
            // ... some code ...
            ArrayJ array1 = ImageJConverters.copyImagePlus2ToArrayJ(inputImageJ, device, MemoryType.BUFFER); // Convert ImageJ ImagePlus to ArrayJ
            ArrayJ array2 = ImgLib2Converters.copyImgToArrayJ(inputImgLib2, device, MemoryType.BUFFER);      // Convert ImgLib2 Img<FloatType> to ArrayJ
            // ... some code ...        
        }
    }

** From ArrayJ to ImageJ and ImgLib2**
.. code:: java

    import net.clesperanto.core.DeviceJ;
    import net.clesperanto.core.ArrayJ;
    import net.clesperanto.core.MemoryType;
    import net.clesperanto.imagej.ImageJConverters;
    import net.clesperanto.imglib2.ImgLib2Converters;

    import net.imglib2.RandomAccessibleInterval;
    import ij.ImagePlus;

    public class MyExampleCode {
        public static void main(String[] args) {
            // ... some code ...
            ImagePlus outputImp = ImageJConverters.copyArrayJToImagePlus(array1);                      // Convert ArrayJ to ImageJ ImagePlus
            RandomAccessibleInterval<FloatType> outputImg = ImgLib2Converters.copyArrayJToImg(array2); // Convert ArrayJ to ImgLib2 Img<FloatType>
            // ... some code ...        
        }
    }    

Execute an Operation
--------------------

Once you have your data on the device in the form of `ArrayJ` objects, you can execute various GPU operations provided by clesperantoJ.
These operations can perform a wide range of image processing and analysis tasks directly on the GPU, leveraging its parallel processing capabilities for improved performance.
They are built as static methods of operation classes, and usually take one or more `ArrayJ` objects as input and produce an output `ArrayJ` objects.

.. code:: java

    import net.clesperanto.core.DeviceJ;
    import net.clesperanto.core.ArrayJ;
    import net.clesperanto.kernels.Tier1;

    public class MyExampleCode {
        public static void main(String[] args) {
            // ... some code ...
            ArrayJ inputArray = // ... initialize and fill input array ...
            ArrayJ outputArray = ArrayJ.create([inputArray.width(), inputArray.height(), inputArray.depth()], device, inputArray.getDataType(), inputArray.getMemoryType());
            Tier1.gaussian_blur(inputArray, outputArray, 2.0f, 2.0f, 2.0f); // Apply Gaussian blur with sigma 2.0
            // ... some code ...        
        }
    }

it is also possible to let the operation create the output ArrayJ for you. In this case, you need to pass null as the output ArrayJ.

.. code:: java

    import net.clesperanto.core.DeviceJ;
    import net.clesperanto.core.ArrayJ;
    import net.clesperanto.kernels.Tier1;

    public class MyExampleCode {
        public static void main(String[] args) {
            // ... some code ...
            ArrayJ inputArray = // ... initialize and fill input array ...
            ArrayJ outputArray = Tier1.gaussian_blur(inputArray, null, 2.0f, 2.0f, 2.0f); // Apply Gaussian blur with sigma 2.0   
            // ... some code ...        
        }
    }

The example operation `gaussian_blur` is a static method of the class `Tier1` located in the package `net.clesperanto.kernels`. The package contains all the available operations organized by tiers from `1` to `8` depending on their complexity.
This organisation is purely for management purposes and operations can be freely mixed together in your code regardless of their tier. See the :doc:`API reference <api/index>` for a full list of available operations and their respective classes.

Execute a mini-pipeline
-----------------------

clesperantoJ allows you to chain multiple operations together to create mini-pipelines that can perform complex image processing tasks in a single execution flow.
This is done by sequentially calling the desired operations, passing the output of one operation as the input to the next.
By doing so, you can build efficient processing pipelines that leverage the GPU's parallel processing capabilities.

.. code:: java

    import net.clesperanto.core.DeviceJ;
    import net.clesperanto.core.ArrayJ;
    import net.clesperanto.kernels.Tier1;
    import net.clesperanto.kernels.Tier5;

    public class MyExampleCode {
        public static void main(String[] args) {
            // ... some code ...
            ArrayJ inputArray = // ... initialize and fill input array ...
            ArrayJ blurredArray = Tier1.gaussian_blur(inputArray, null, 2.0f, 2.0f, 2.0f);
            ArrayJ thresholdedArray = Tier4.threshold_otsu(blurredArray, null);
            ArrayJ edgeDetectedArray = Tier5.connected_component_labeling(thresholdedArray, null);
            // ... some code ...        
        }
    }
