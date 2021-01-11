import io

from google.cloud import videointelligence_v1 as videointelligence
import detector


def detect_person(local_file_path="path/to/your/video-file.mp4"):
    """Detects people in a video from a local file."""

    client = videointelligence.VideoIntelligenceServiceClient()

    with io.open(local_file_path, "rb") as f:
        input_content = f.read()

    # Configure the request
    config = videointelligence.types.PersonDetectionConfig(
        include_bounding_boxes=True,
        include_attributes=True,
        include_pose_landmarks=True,
    )

    context = videointelligence.types.VideoContext(person_detection_config=config)

    # Start the asynchronous request
    operation = client.annotate_video(
        request={
            "features": [videointelligence.Feature.LOGO_RECOGNITION, videointelligence.Feature.LABEL_DETECTION, videointelligence.Feature.PERSON_DETECTION, videointelligence.Feature.FACE_DETECTION, videointelligence.Feature.EXPLICIT_CONTENT_DETECTION],
            "input_content": input_content,
            "video_context": context,
        }
    )

    print("\nProcessing video for person detection annotations.")
    result = operation.result(timeout=300)

    print("\nFinished processing.\n")

    # Retrieve the first result, because a single video was processed.
    annotation_result = result.annotation_results[0]
    
    print("Searching for people...")
    detector.person(annotation_result)
    
    print("Searching for explicit content...")
    detector.explicit(annotation_result)
    
    print("Searching for visage...")
    detector.visage(annotation_result)
    
    print("Searching for logo...")
    detector.logo(annotation_result)

detect_person("videos/#cocacola/1.mp4")