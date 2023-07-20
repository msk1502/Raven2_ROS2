import launch
import launch_ros.actions
from launch.actions import DeclareLaunchArgument ExecuteProcess
from launch.substitutions import LaunchConfiguration

def generate_launch_description():
    
    model_value = LaunchConfiguration('model')
    model_arg = DeclareLaunchArgument(
        'model',
        default='$(find raven_2_params)/data/ravenII_gold_arm.urdf'
    )
    raven_2_node = launch_ros.actions.Node(
        package='raven_2',
        excutable='rt_process_preempt',
        name='raven_2',
        parameters="$(find raven_2)/params/r2params.yaml",
    )
    robot_state_publisher_node = launch_ros.actions.Node(
        package='robot_state_publisher'
        excutable='sate_publisher'
        name='robot_state_publisher'
    )

    model_conditioned = ExcuteProcess(
        cmd=[[
            'ros2 param set ',
            '/raven_2 model ',
            model_arg
        ]]
    )
    return launch.LaunchDescription([
        model_arg,
        raven_2_node,
        robot_state_publisher_node,
        model_conditioned
    ])
