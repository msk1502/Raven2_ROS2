cmake_minimum_required (VERSION 2.8.3)
project(raven_2)

set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} "${CMAKE_CURRENT_SOURCE_DIR}/cmake/Modules/")

find_package(ament_cmake REQUIRED COMPONENTS
  rclcpp
  rclpy
  message_generation
  dynamic_reconfigure
  std_msgs
  sensor_msgs
  geometry_msgs
  tf
)

find_package(
  Eigen3 REQUIRED
  rosidl_default_generators REQUIRED
  raven_automove.msg REQUIRED
  raven_state.msg REQUIRED
)

rosidl_generate_interfaces(${raven_2}
  ${msg_files}
  DEPENDENCIES raven_automove.msg raven_state.msg 
)
add_message_files(
  DIRECTORY msg
  FILES raven_automove.msg raven_state.msg
)

rosidl_generate_interfaces(
  DEPENDENCIES std_msgs geometry_msgs
)

generate_dynamic_reconfigure_options(
  cfg/Raven2.cfg
)

ament_export_dependencies(
  rclcpp
  dynamic_reconfigure
  tf
)

ament_export_libraries(
  include
  include/raven
  ${catkin_INCLUDE_DIRS}
  ${EIGEN3_INCLUDE_DIR}
)

if(CMAKE_COMPILER_IS_GNUCXX)
  set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wall")
endif()

set(r2_control_sources
  src/raven/console_process.cpp
  src/raven/dof.cpp
  src/raven/fwd_cable_coupling.cpp
  src/raven/get_USB_packet.cpp
  src/raven/globals.cpp
  src/raven/grav_comp.cpp
  src/raven/homing.cpp
  src/raven/init.cpp
  src/raven/inv_cable_coupling.cpp
  src/raven/local_io.cpp
  src/raven/log.cpp
  src/raven/mapping.cpp
  src/raven/network_layer.cpp
  src/raven/overdrive_detect.cpp
  src/raven/pid_control.cpp
  src/raven/put_USB_packet.cpp
  src/raven/r2_jacobian.cpp
  src/raven/r2_kinematics.cpp
  src/raven/reconfigure.cpp
  src/raven/rt_process_preempt.cpp
  src/raven/rt_raven.cpp
  src/raven/state_estimate.cpp
  src/raven/state_machine.cpp
  src/raven/t_to_DAC_val.cpp
  src/raven/tools.cpp
  src/raven/trajectory.cpp
  src/raven/update_atmel_io.cpp
  src/raven/update_device_state.cpp
  src/raven/USB_init.cpp
  src/raven/utils.cpp
  CMAKE_CXX_STANDARD 14
)

add_executable(r2_control ${r2_control_sources})
add_dependencies(r2_control ${${PROJECT_NAME}_EXPORTED_TARGETS})
target_link_libraries(r2_control ${catkin_LIBRARIES})

install(DIRECTORY
  launch
  DESTINATION share/${raven_2}/
)

ament_package()