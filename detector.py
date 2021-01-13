from google.cloud import videointelligence_v1 as videointelligence

##########################################
######## person
##########################################
def person(annotation_result):
    for annotation in annotation_result.person_detection_annotations:
        print("Person detected:")
        for track in annotation.tracks:
            # Attributes include unique pieces of clothing,
            # poses, or hair color.
            print("Attributes:")
            for attribute in timestamped_object.attributes:
                print(
                    "\t{}:{} {}".format(
                        attribute.name, attribute.value, attribute.confidence
                    )
                )

            # Landmarks in person detection include body parts such as
            # left_shoulder, right_ear, and right_ankle
            print("Landmarks:")
            for landmark in timestamped_object.landmarks:
                print(
                    "\t{}: {} (x={}, y={})".format(
                        landmark.name,
                        landmark.confidence,
                        landmark.point.x,  # Normalized vertex
                        landmark.point.y,  # Normalized vertex
                    )
                )

##########################################
######## FACE
##########################################
def visage(annotation_result):
    for annotation in annotation_result.face_detection_annotations:
        print("Face detected:")
        for track in annotation.tracks:
            # Attributes include glasses, headwear, smiling, direction of gaze
            print("Attributes:")
            for attribute in timestamped_object.attributes:
                print(
                    "\t{}:{} {}".format(
                        attribute.name, attribute.value, attribute.confidence
                    )
                )

##########################################
######## theme
##########################################
def theme(annotation_result):
    # Process video/segment level label annotations
    videos_desc = []
    segment_labels = annotation_result.segment_label_annotations
    for i, segment_label in enumerate(segment_labels):
        for i, segment in enumerate(segment_label.segments):
            confidence = segment.confidence
            if confidence >= 0.7 :
                videos_desc.append(segment_label.entity.description)
    
    return videos_desc

##########################################
######## explicit
##########################################
def explicit(annotation_result):
    full = []
    for frame in annotation_result.explicit_annotation.frames:
        likelihood = videointelligence.Likelihood(frame.pornography_likelihood)
        frame_time = frame.time_offset.seconds + frame.time_offset.microseconds / 1e6
        full.append(likelihood.name)
            
    if "VERY_LIKELY" in full:
        return "VERY_LIKELY"
    if "LIKELY" in full:
        return "LIKELY"
    if "POSSIBLE" in full:
        return "POSSIBLE"


##########################################
######## logo
##########################################
def logo(annotation_result):
    logos = []
    # Annotations for list of logos detected, tracked and recognized in video.
    for logo_recognition_annotation in annotation_result.logo_recognition_annotations:
        entity = logo_recognition_annotation.entity
        for track in logo_recognition_annotation.tracks:
            confidence = track.confidence
            if confidence > 0.92:
                logos.append(entity.description)
    return logos