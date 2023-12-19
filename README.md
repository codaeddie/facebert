### Project Tree and Progress Overview

#### 1. Data Preparation
-   **Script**: `prepare_data.py`
-   **Status**: Not yet implemented.
-   **Next Steps**: Implement a script to format and prepare test data for model processing.

#### 2. Model Evaluation Scripts
-   Scripts
    -   `bert_evaluation.py`
    -   `crammedbert_evaluation.py`
    -   `ultrafastbert_evaluation.py`
-   **Status**: Not yet implemented.
-   **Next Steps**: Create scripts to process test data through each model and generate model outputs.
#### 3. Entropy Sequence Generation
-   **Script**: `generate_entropy_sequences.py` (based on `run_entropy.py` and `run_entropy_batch.py`)
-   **Status**: Initial template set up.
-   **Next Steps**: Fully implement the script, ensuring compatibility with our models and testing it with actual model outputs.
#### 4. Fourier Transformation
-   **Script**: `apply_fourier_transformation.py` (based on `run_fft.py`)
-   **Status**: Fully implemented based on the provided pseudocode.
-   **Next Steps**: Integrate this script with the output of the entropy sequence generation script and test it.
#### 5. FACE Score Calculation
-   **Script**: `calculate_face_scores.py`
-   **Status**: Template created with placeholders for FACE metrics computation.
-   **Next Steps**: Implement the actual logic for calculating FACE scores, including Pearson Correlation, Spearman Rank Correlation, Spectral Overlap, and Spectral Angle Mapper.
#### 6. Visualization and Analysis
-   **Script**: `visualize_results.py`
-   **Status**: Not yet implemented.
-   **Next Steps**: Develop a script for visualizing the results and analyzing the performance of each model.
#### 7. Utilities
-   **Script**: `utils.py`
-   **Status**: Not yet implemented.
-   **Next Steps**: Create utility functions for common tasks like data loading and logging.
#### 8. Main Execution Script
-   **Script**: `run_evaluation.py`
-   **Status**: Not yet implemented.
-   **Next Steps**: Develop a script to orchestrate the entire evaluation process, calling the scripts in sequence and managing the flow of data.
### Overall Project Status
We have made significant progress in setting up the core scripts for entropy sequence generation and Fourier transformation. The FACE score calculation script is in place with a structure, awaiting the implementation of the actual metrics calculation. The remaining parts of the project, including data preparation, model-specific evaluation scripts, result visualization, and the main execution script, are yet to be developed.

Our next focus should be on completing the implementation of the entropy sequence generation script and then moving on to the FACE score calculation logic. Simultaneously, we can start working on the data preparation and model evaluation scripts to ensure a smooth flow of data through t
