from utils import read_video,save_video
from trackers import Tracker
import cv2
from team_assigner import TeamAssigner 
from player_ball_assigner import PlayerBallAssigner


def main():
    #read video 
    video_frames = read_video('input/08fd33_4.mp4')

    #initialize Tracker
    tracker= Tracker('models/best.pt')
    
    tracks = tracker.get_object_tracks(video_frames,
                                       read_from_stub=True,
                                       stub_path='stubs/track_stubs.pkl')
    
    #interpolate ball positions 
    tracks["ball"]=tracker.interpolate_ball_positions(tracks["ball"])

    #Assign Player Teams
    team_assigner = TeamAssigner()
    team_assigner.assign_team_color(video_frames[0],tracks['players'][0])
    
    for frame_num,player_track in enumerate(tracks['players']):
        for player_id,track in player_track.items():
            team = team_assigner.get_player_team(video_frames[frame_num],
                                                 track['bbox'],
                                                 player_id)
            tracks['players'][frame_num][player_id]['team'] = team
            tracks['players'][frame_num][player_id]['team_color'] = team_assigner.team_colors[team]


    # Assign Ball Aquisition
    player_assigner =PlayerBallAssigner()
    for frame_num, player_track in enumerate(tracks['players']):
        ball_bbox = tracks['ball'][frame_num][1]['bbox']
        assigned_player = player_assigner.assign_ball_to_player(player_track, ball_bbox)

        if assigned_player != -1:
            tracks['players'][frame_num][assigned_player]['has_ball'] = True


    #Draw output 
    ##Draw Object Tracks 
    output_videos_frames=tracker.draw_annotations(video_frames,tracks)

    #save video
    save_video(output_videos_frames,'output_videos/output_video.avi')




if __name__ == '__main__':
    main()