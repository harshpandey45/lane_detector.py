# 🚗 Advanced Computer Vision ADAS: Real-Time Road Lane Detection Mechanism

> A robust computer vision perception pipeline built from scratch using Python and OpenCV to convert raw roadway RGB frames into drivable lane boundary estimates in real time.

---

## 📌 Project Overview
In modern Advanced Driver Assistance Systems (ADAS) and Autonomous Vehicles, reliable lane estimation is the foundational building block for path planning and lane-keeping control. This project implements a classical perception pipeline that processes sequential road frames, isolates the region of interest, extracts structural edge gradients, and utilizes polar-space transformations to project a clear drivable corridor onto the vehicle's perspective.

---

## 🛠️ Complete System Architecture & Pipeline Flow
The system executes a 5-stage sequential pipeline to filter uncertainty and extract structural road geometry:

1. **Capture & Preprocessing:** Converts high-resolution RGB frames to single-channel Grayscale and applies **Gaussian Blur ($5\times5$ kernel)** to suppress high-frequency asphalt texture and sensor noise.
2. **Edge Extraction (Canny Operator):** Computes image intensity gradients via Sobel derivatives followed by Non-Maximum Suppression and Hysteresis Thresholding to extract thin, noise-free edge boundaries.
3. **Spatial Region of Interest (ROI) Masking:** Applies a dynamic trapezoidal binary polygon mask via bitwise operations to completely eliminate irrelevant visual clutter (sky, horizon, trees, and roadside obstacles).
4. **Hough Voting & Line Fitting:** Executes **Probabilistic Hough Transform (`HoughLinesP`)** in polar coordinate space ($\rho, \theta$) to map edge points into intersecting sinusoidal curves, grouping segments by slope thresholds.
5. **Extrapolation & Projection:** Combines linear regression (`np.polyfit`) to bridge dashed/broken markings into solid continuous boundary lines and blends them back onto the original frame using semi-transparent weighted overlays.

---

## 🧮 Core Mathematical Foundation
To prevent infinite slope division errors ($m \to \infty$) common in standard Cartesian equations ($y = mx + c$) for vertical lines, the system formulates line detection using **Polar Normal Form**:

$$x \cos(\theta) + y \sin(\theta) = \rho$$

* Every edge pixel $(x, y)$ in image space maps to a unique sinusoidal curve in Hough parameter space $(\rho, \theta)$.
* Accumulator intersections indicate points of strong collinear agreement across multiple edge points, isolating true lane boundaries.

---

## ⚙️ Tech Stack & Dependencies
* **Language:** Python 3.x
* **Core Vision Library:** OpenCV (`cv2`) — for gradient transformations, masking, and Hough transforms.
* **Mathematical Compute:** NumPy — for array matrix operations, polygon coordinate vertices, and polynomial line fitting (`np.polyfit`).

---

## 🚀 Getting Started & Installation

1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/harshpandey45/road-lane-detector.git](https://github.com/harshpandey45/road-lane-detector.git)
   cd road-lane-detector
