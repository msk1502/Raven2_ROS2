import launch
import launch_ros.actions

def generate_launch_description():
    return launch.LaunchDescription([
        launch_ros.actions.Node(
            package='raven_2',
            excutable='rt_process_preempt',
            name='raven_2',
            parameters="$(find raven_2)/params/r2params.yaml",
        )
    ])
