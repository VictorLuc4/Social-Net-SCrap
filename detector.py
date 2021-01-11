from google.cloud import videointelligence_v1 as videointelligence

def person(annotation_result):
    for annotation in annotation_result.person_detection_annotations:
        print("Person detected:")
        for track in annotation.tracks:
            print(
                "Segment: {}s to {}s".format(
                    track.segment.start_time_offset.seconds
                    + track.segment.start_time_offset.microseconds / 1e6,
                    track.segment.end_time_offset.seconds
                    + track.segment.end_time_offset.microseconds / 1e6,
                )
            )

            # Each segment includes timestamped objects that include
            # characteristic - -e.g.clothes, posture of the person detected.
            # Grab the first timestamped object
            timestamped_object = track.timestamped_objects[0]
            box = timestamped_object.normalized_bounding_box
            print("Bounding box:")
            print("\tleft  : {}".format(box.left))
            print("\ttop   : {}".format(box.top))
            print("\tright : {}".format(box.right))
            print("\tbottom: {}".format(box.bottom))

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
            print(
                "Segment: {}s to {}s".format(
                    track.segment.start_time_offset.seconds
                    + track.segment.start_time_offset.microseconds / 1e6,
                    track.segment.end_time_offset.seconds
                    + track.segment.end_time_offset.microseconds / 1e6,
                )
            )

            # Each segment includes timestamped faces that include
            # characteristics of the face detected.
            # Grab the first timestamped face
            timestamped_object = track.timestamped_objects[0]
            box = timestamped_object.normalized_bounding_box
            print("Bounding box:")
            print("\tleft  : {}".format(box.left))
            print("\ttop   : {}".format(box.top))
            print("\tright : {}".format(box.right))
            print("\tbottom: {}".format(box.bottom))

            # Attributes include glasses, headwear, smiling, direction of gaze
            print("Attributes:")
            for attribute in timestamped_object.attributes:
                print(
                    "\t{}:{} {}".format(
                        attribute.name, attribute.value, attribute.confidence
                    )
                )

def explicit(annotation_result):
    print("Explicit content detection")
    for frame in annotation_result.explicit_annotation.frames:
        likelihood = videointelligence.Likelihood(frame.pornography_likelihood)
        frame_time = frame.time_offset.seconds + frame.time_offset.microseconds / 1e6
        print("Time: {}s".format(frame_time))
        print("\tpornography: {}".format(likelihood.name))


def logo(annotation_result):
    # Annotations for list of logos detected, tracked and recognized in video.
    for logo_recognition_annotation in annotation_result.logo_recognition_annotations:
        entity = logo_recognition_annotation.entity

        # Opaque entity ID. Some IDs may be available in [Google Knowledge Graph
        # Search API](https://developers.google.com/knowledge-graph/).
        print(u"Entity Id : {}".format(entity.entity_id))

        print(u"Description : {}".format(entity.description))

        # All logo tracks where the recognized logo appears. Each track corresponds
        # to one logo instance appearing in consecutive frames.
        for track in logo_recognition_annotation.tracks:
            # Video segment of a track.
            print(
                u"\n\tStart Time Offset : {}.{}".format(
                    track.segment.start_time_offset.seconds,
                    track.segment.start_time_offset.microseconds * 1000,
                )
            )
            print(
                u"\tEnd Time Offset : {}.{}".format(
                    track.segment.end_time_offset.seconds,
                    track.segment.end_time_offset.microseconds * 1000,
                )
            )
            print(u"\tConfidence : {}".format(track.confidence))

            # The object with timestamp and attributes per frame in the track.
            #for timestamped_object in track.timestamped_objects:

                # Normalized Bounding box in a frame, where the object is located.
                #normalized_bounding_box = timestamped_object.normalized_bounding_box
                #print(u"\n\t\tLeft : {}".format(normalized_bounding_box.left))
                #print(u"\t\tTop : {}".format(normalized_bounding_box.top))
                #print(u"\t\tRight : {}".format(normalized_bounding_box.right))
                #print(u"\t\tBottom : {}".format(normalized_bounding_box.bottom))

                # Optional. The attributes of the object in the bounding box.
                #for attribute in timestamped_object.attributes:
                #    print(u"\n\t\t\tName : {}".format(attribute.name))
                #    print(u"\t\t\tConfidence : {}".format(attribute.confidence))
                #    print(u"\t\t\tValue : {}".format(attribute.value))

            # Optional. Attributes in the track level.
            #for track_attribute in track.attributes:
            #    print(u"\n\t\tName : {}".format(track_attribute.name))
            #    print(u"\t\tConfidence : {}".format(track_attribute.confidence))
            #    print(u"\t\tValue : {}".format(track_attribute.value))

        # All video segments where the recognized logo appears. There might be
        # multiple instances of the same logo class appearing in one VideoSegment.
        #for segment in logo_recognition_annotation.segments:
        #    print(
        #        u"\n\tStart Time Offset : {}.{}".format(
        #            segment.start_time_offset.seconds,
        #            segment.start_time_offset.microseconds * 1000,
        #        )
        #    )
        #    print(
        #        u"\tEnd Time Offset : {}.{}".format(
        #            segment.end_time_offset.seconds,
        #            segment.end_time_offset.microseconds * 1000,
        #        )
        #    )